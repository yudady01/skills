package com.galaxy.handler.downloadReportHandler.impl;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.galaxy.domain.UserDomainService;
import com.galaxy.enumeration.ReportType;
import com.galaxy.feign.client.basics.BasicsReportFeignClient;
import com.galaxy.handler.downloadReportHandler.DownloadReportHandler;
import com.galaxy.model.dto.ReportUpdateDto;
import com.galaxy.model.dto.UserQryDto;
import com.galaxy.model.vo.LockStatusVo;
import com.galaxy.model.vo.ReportQryVo;
import com.galaxy.model.vo.UserBalanceVo;
import com.galaxy.model.vo.UserExportVo;
import com.galaxy.model.vo.UserRowVo;
import com.galaxy.module.model.vo.PageVo;
import com.galaxy.util.ReportMaskFactory;
import java.math.BigDecimal;
import java.util.List;
import java.util.stream.Collectors;
import lombok.NonNull;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.apache.commons.lang3.ObjectUtils;
import org.springframework.stereotype.Component;


import static com.galaxy.util.ReportConvertUtils.convertString;

@Slf4j
@Component
@RequiredArgsConstructor
public class UserQueryReport implements DownloadReportHandler {

    private final BasicsReportFeignClient basicsFeignClient;
    private final UserDomainService userDomainService;
    private final ObjectMapper mapper;
    private static final long DOWNLOAD_ONE_PAGE_SIZE_MAX = 500;

    @Override
    public ReportType type() {
        return ReportType.PLT_USER_QUERY_DOWNLOAD;
    }

    @Override
    public void handle(ReportQryVo qryVo) {
        log.info("[PLT_USER_QUERY_DOWNLOAD], START");
        UserQryDto userQryDto = mapper.convertValue(qryVo.getSearchParam(), UserQryDto.class);
        long page = 0;

        ReportUpdateDto dto = new ReportUpdateDto();
        dto.setId(qryVo.getId());
        dto.setReportExportType("CSV");
        dto.setTitles(List.of("帳戶名", "手機號", "上級代理", "客服團隊", "VIP層級", "狀態", "幣種", "錢包餘額", "剩餘提現流水", "剩餘平台限制流水", "出款標籤", "註冊時間", "上次登入時間", "備註"));

        ReportMaskFactory factory = ReportMaskFactory.get(mapper, qryVo.getUnmaskAuths());

        PageVo<UserExportVo> pageVo = null;
        do {
            userQryDto.setPage(++page);
            userQryDto.setSize(DOWNLOAD_ONE_PAGE_SIZE_MAX);
            PageVo<UserRowVo> lists = userDomainService.qryUsers(userQryDto, userQryDto.getIsOnline(), userQryDto.getIsWhiteList(), userQryDto.getCurrency());
            pageVo = assembleUserRows(lists, factory);
            dto.setRows(createUserExportVoCsvRowsData(pageVo.getRecords()));
            dto.setCurrentPage(pageVo.getCurrent().intValue());
            dto.setTotalPage(pageVo.getPages().intValue());
            basicsFeignClient.makeReportDocument(dto);
        } while (!pageVo.getRecords().isEmpty() && ObjectUtils.notEqual(pageVo.getPages(), pageVo.getCurrent()));
        factory.finish();
        log.info("[PLT_USER_QUERY_DOWNLOAD], END");
    }

    private PageVo<UserExportVo> assembleUserRows(PageVo<UserRowVo> rows, ReportMaskFactory factory) {


        List<UserExportVo> exportList = rows.getRecords()
            .stream()
            .peek(factory::check)
            .map(this::convertToUserExportVo)

            .collect(Collectors.toList());

        return new PageVo<>(rows.getCurrent(), rows.getSize(), rows.getTotal(), rows.getPages(), exportList);
    }

    private UserExportVo convertToUserExportVo(UserRowVo row) {
        UserExportVo export = new UserExportVo();
        export.setUsername(row.getUsername());
        export.setTelephone(row.getTelephone());
        export.setParentName(row.getParentName());
        export.setServiceTeams(row.getServiceTeam() == 1 ? "客服團隊一" : "客服團隊二");
        export.setVipName(row.getVipName());
        export.setStatus(convertStatus(row.getLockStatus()));
        export.setCurrency(row.getCurrency());
        export.setWithdrawTag(row.getWithdrawTag());
        export.setLeftWithdrawWater(row.getLeftWithdrawWater());
        export.setLeftWithdrawLimitWater(row.getLeftWithdrawLimitWater());
        export.setRegisterTime(row.getRegisterTime());
        export.setLastLoginTime(row.getLastLoginTime());
        export.setRemark(row.getRemark());
        // 計算使用者的餘額
        if (null != row.getBalanceList()) {
            BigDecimal balance = row.getBalanceList()
                .stream()
                .filter(v -> v.getCurrency().equals(export.getCurrency()))
                .map(UserBalanceVo::getBalance)
                .reduce(BigDecimal.ZERO, BigDecimal::add);
            export.setBalance(balance);

        }

        return export;
    }

    private String convertStatus(List<LockStatusVo> lockStatus) {
        if (lockStatus == null) {
            return "未知";
        }
        for (LockStatusVo status : lockStatus) {
            if (status.isLock()) {
                return "鎖定";
            }
        }
        return "正常";
    }


    private List<List<String>> createUserExportVoCsvRowsData(@NonNull List<UserExportVo> data) {
        return data.stream()
            .map(this::createCsvRowsData)
            .collect(Collectors.toList());
    }

    private List<String> createCsvRowsData(@NonNull UserExportVo userExportVo) {
        return List.of(
            convertString(userExportVo.getUsername()),
            convertString(userExportVo.getTelephone()),
            convertString(userExportVo.getParentName()),
            convertString(userExportVo.getServiceTeams()),
            convertString(userExportVo.getVipName()),
            convertString(userExportVo.getStatus()),
            convertString(userExportVo.getCurrency()),
            convertString(userExportVo.getBalance()),
            convertString(userExportVo.getLeftWithdrawWater()),
            convertString(userExportVo.getLeftWithdrawLimitWater()),
            convertString(userExportVo.getWithdrawTag()),
            convertString(userExportVo.getRegisterTime()),
            convertString(userExportVo.getLastLoginTime()),
            convertString(userExportVo.getRemark())
        );
    }

}
