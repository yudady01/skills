package com.galaxy.handler.downloadReportHanlder.impl;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.galaxy.domain.WithdrawManageDomainService;
import com.galaxy.enumeration.OsType;
import com.galaxy.enumeration.basics.ReportType;
import com.galaxy.enumeration.fund.WithdrawStatus;
import com.galaxy.feign.client.basic.BasicFeignClient;
import com.galaxy.handler.downloadReportHanlder.DownloadReportHandler;
import com.galaxy.model.basic.dto.ReportUpdateDto;
import com.galaxy.model.basic.vo.ReportQryVo;
import com.galaxy.model.fund.withdraw.dto.QueryWithdrawSummaryDto;
import com.galaxy.model.fund.withdraw.vo.WithdrawChildVo;
import com.galaxy.model.fund.withdraw.vo.WithdrawVo;
import com.galaxy.module.enumeration.UserType;
import com.galaxy.module.model.vo.PageVo;
import com.galaxy.utils.ReportMaskFactory;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Component;
import org.springframework.util.CollectionUtils;


import static com.galaxy.module.constant.HeaderKey.H_KEY_CURRENCY;
import static com.galaxy.module.constant.HeaderKey.H_KEY_LANGUAGE;
import static com.galaxy.utils.ReportConvertUtils.convertString;

/**
 * @author hardy
 */
@Slf4j
@Component
@RequiredArgsConstructor
public class WithdrawSummaryReport implements DownloadReportHandler {
    private final static long MAX_SIZE = 500L;
    private final WithdrawManageDomainService withdrawManageDomainService;
    private final BasicFeignClient basicFeignClient;

    private final static long START_PAGE = 1L;
    private final ObjectMapper mapper;

    @Override
    public ReportType type() {
        return ReportType.PLT_REPORT_WITHDRAW_SUMMARY_DOWNLOAD;
    }

    @Override
    public void handle(ReportQryVo qryVo) {
        log.info("[PLT_REPORT_WITHDRAW_SUMMARY_DOWNLOAD], START");

        QueryWithdrawSummaryDto queryDto = mapper.convertValue(qryVo.getSearchParam(), QueryWithdrawSummaryDto.class);
        Integer timezone = qryVo.getTimezone();
        String language = String.valueOf(qryVo.getSearchParam().get(H_KEY_LANGUAGE));
        String currency = String.valueOf(qryVo.getSearchParam().get(H_KEY_CURRENCY));
        log.info("[WithdrawSummaryReport], queryDto:{} ,language={} ", queryDto, language);
        queryDto.setPage(START_PAGE);
        queryDto.setSize(MAX_SIZE);

        long current;
        long pages;
        PageVo<WithdrawVo> pageVo;

        ReportMaskFactory factory = ReportMaskFactory.get(mapper, qryVo.getUnmaskAuths());

        do {
            pageVo = withdrawManageDomainService.findSummaryList(language, queryDto, currency);

            makeReport(qryVo, pageVo, pageVo.getPages(), pageVo.getCurrent(), timezone, factory);

            current = pageVo.getCurrent() + 1;
            queryDto.setPage(current);

            pages = pageVo.getPages();
        } while (!pageVo.getRecords().isEmpty() && current <= pages);
        factory.finish();
        log.info("[PLT_REPORT_WITHDRAW_SUMMARY_DOWNLOAD], END");
    }

    private void setChildRows(List<List<String>> rows, WithdrawVo parent, List<WithdrawChildVo> subList, Integer timezone) {

        if (!CollectionUtils.isEmpty(subList)) {

            for (WithdrawChildVo record : subList) {
                List<String> row = new ArrayList<>();

                // 托售時間
                row.add(convertString(record.getCreateTime(), timezone, "--"));
                // 托售單號
                row.add(record.getOrderId());
                // 托售子單號
                row.add(record.getOrderSubId());
                // 用戶類型
                row.add(record.getUserType().equals(UserType.CLIENT.getClientType()) ? "會員" : "代理");
                // 托售類型
                row.add(record.getUserType().equals(UserType.CLIENT.getClientType()) ? "托售" : "提佣");
                // 帳戶名
                row.add(record.getUsername());
                // 群組名稱
                row.add("");
                // 上級代理
                row.add("");
                // 托售下分幣種
                row.add("");
                // 托售下分匯率
                row.add("");
                // 托售下分金額
                row.add("");
                // 玩家姓名
                row.add(record.getName());
                // 托售方式
                row.add(record.getWithdrawMode() == 0 ? "傳統託售" : "數字貨幣提幣");
                // 狀態
                row.add(WithdrawStatus.valueOf(record.getStatus()).getName());
                // 出款商戶
                row.add(Optional.ofNullable(record.getChannelMerchantAccountName()).orElse("--"));
                // 出款商戶號
                row.add(Optional.ofNullable(record.getMerchantCode()).orElse("--"));
                // 幣種
                row.add(record.getCurrency());
                // 實際出款
                row.add(convertString(record.getAmount()));
                // 手續費
                row.add(convertString(record.getFee()));
                // 代理金流費
                row.add("");
                // 玩家銀行名稱
                row.add(convertString(record.getBankName(), "--"));
                // 玩家銀行卡號
                row.add(convertString(record.getCardNo(), "--"));
                // 玩家銀行開戶行地址
                row.add(convertString(record.getAddress(), "--"));
                // 玩家錢包地址
                row.add(convertString(record.getUsdtAddress(), "--"));
                // 玩家錢包協議
                row.add(convertString(record.getUsdtProtocol(), "--"));
                // 玩家錢包備註名
                row.add(convertString(record.getUsdtRemark(), "--"));
                // 交易所錢包:錢包地址
                row.add(convertString(record.getTransCenterAddress(), "--"));
                // 交易所錢包:名稱
                row.add(convertString(record.getTransCenterNameDesc(), "--"));
                // 交易所錢包:備註
                row.add(convertString(record.getTransCenterRemark(), "--"));
                // VIP等級
                row.add(parent.getVipName());
                // 操作端
                row.add(OsType.valueOf(parent.getClientType()).getDesc());
                // 審核分配員
                row.add(convertString(record.getFirstDispatcher(), "--"));
                // 審核分配備註
                row.add(convertString(record.getFirstDispatchRemark(), "--"));
                // 審核分配時間
                row.add(convertString(record.getFirstDispatchTime(), timezone, "--"));
                // 出款審核員
                row.add(convertString(record.getApprover(), "--"));
                // 出款審核備註
                row.add(convertString(record.getApproveRemark(), "--"));
                // 出款審核時間
                row.add(convertString(record.getApproveTime(), timezone, "--"));
                // 出款分配員
                row.add(Optional.ofNullable(record.getSecondDispatcher()).orElse("--"));
                // 出款分配備註
                row.add(Optional.ofNullable(record.getSecondDispatchRemark()).orElse("--"));
                // 出款分配時間
                row.add(convertString(record.getSecondDispatchTime(), timezone));
                // 出款人
                row.add(Optional.ofNullable(record.getPayer()).orElse("--"));
                // 出款備註
                row.add(Optional.ofNullable(record.getPayRemark()).orElse("--"));
                // 出款時間
                row.add(convertString(record.getPayTime(), timezone, "--"));
                // 異常托售處理備註
                // row.add(convertString(record.getRiskApvRemark(), "--"));
                // 異常出款備註
                row.add(convertString(record.getPayExceptionRemark(), "--"));
                // 請求資訊
                row.add("--");

                rows.add(row);
            }
        }
    }

    private List<List<String>> createCsvRowsData(List<WithdrawVo> records, Integer timezone, ReportMaskFactory factory) {
        List<List<String>> rows = new ArrayList<>();

        for (WithdrawVo record : records) {

            factory.check(record);

            List<String> row = new ArrayList<>();

            // 托售時間
            row.add(convertString(record.getCreateTime(), timezone, "--"));
            // 托售單號
            row.add(record.getOrderId());
            // 托售子單號
            row.add("--");
            // 用戶類型
            row.add(record.getUserType().equals(UserType.CLIENT.getClientType()) ? "會員" : "代理");
            // 托售類型
            row.add(record.getUserType().equals(UserType.CLIENT.getClientType()) ? "托售" : "提傭");
            // 帳戶名
            row.add(record.getUsername());
            // 群組名稱
            row.add(record.getGroupName());
            // 上級代理
            row.add(record.getProxyAccount());
            // 托售下分幣種
            row.add(record.getExchangeCurrency());
            // 托售下分匯率
            row.add(convertString(record.getExchangeRate()));
            // 托售下分金額
            row.add(convertString(record.getExchangeAmount()));
            // 玩家姓名
            row.add(record.getName());
            // 托售方式
            row.add(record.getWithdrawMode() == 0 ? "傳統託售" : "數字貨幣提幣");
            // 狀態
            row.add(WithdrawStatus.valueOf(record.getStatus()).getName());
            // 出款商戶
            row.add("--");
            // 出款商戶號
            row.add("--");
            // 幣種
            row.add(record.getCurrency());
            // 實際出款
            row.add(convertString(record.getAmount()));
            // 手續費
            row.add(convertString(record.getFee()));
            // 代理金流費
            row.add(convertString(record.getProxyPaymentFee()));
            // 玩家銀行名稱
            row.add(convertString(record.getBankName(), "--"));
            // 玩家銀行卡號
            row.add(convertString(record.getCardNo(), "--"));
            // 玩家銀行開戶行地址
            row.add(convertString(record.getAddress(), "--"));
            // 玩家錢包地址
            row.add(convertString(record.getUsdtAddress(), "--"));
            // 玩家錢包協議
            row.add(convertString(record.getUsdtProtocol(), "--"));
            // 玩家錢包備註名
            row.add(convertString(record.getUsdtRemark(), "--"));
            // 交易所錢包:錢包地址
            row.add(convertString(record.getTransCenterAddress(), "--"));
            // 交易所錢包:名稱
            row.add(convertString(record.getTransCenterNameDesc(), "--"));
            // 交易所錢包:備註
            row.add(convertString(record.getTransCenterRemark(), "--"));
            // VIP等級
            row.add(record.getVipName());
            // 操作端
            row.add(OsType.valueOf(record.getClientType()).getDesc());
            // 審核分配員
            row.add(convertString(record.getFirstDispatcher(), "--"));
            // 審核分配備註
            row.add(convertString(record.getFirstDispatchRemark(), "--"));
            // 審核分配時間
            row.add(convertString(record.getFirstDispatchTime(), timezone, "--"));
            // 出款審核員
            row.add(convertString(record.getApprover(), "--"));
            // 出款審核備註
            row.add(convertString(record.getApproveRemark(), "--"));
            // 出款審核時間
            row.add(convertString(record.getApproveTime(), timezone, "--"));
            // 出款分配員
            row.add("--");
            // 出款分配備註
            row.add("--");
            // 出款分配時間
            row.add("--");
            // 出款人
            row.add("--");
            // 出款備註
            row.add("--");
            // 出款時間
            row.add("--");
            // 異常托售處理備註
            // row.add(convertString(record.getRiskApvRemark(), "--"));
            // 異常出款備註
            row.add(convertString(record.getPayExceptionRemark(), "--"));
            // 請求資訊
            row.add("--");

            rows.add(row);
            setChildRows(rows, record, record.getSubList(), timezone);
        }
        return rows;
    }

    private ReportUpdateDto getReportUpdateDto(ReportQryVo qryVo, PageVo<WithdrawVo> pageVo, Long totalPage, Long currentPage, Integer timezone, ReportMaskFactory factory) {
        ReportUpdateDto reportUpdateDto = new ReportUpdateDto();
        reportUpdateDto.setId(qryVo.getId());
        reportUpdateDto.setReportExportType("CSV");
        reportUpdateDto.setTitles(List.of("托售時間",
            "托售單號",
            "托售子單號",
            "用戶類型",
            "托售類型",
            "帳戶名",
            "群組名稱",
            "上級代理",
            "托售下分幣種",
            "托售匯率",
            "托售下分金額",
            "玩家姓名",
            "托售方式",
            "狀態",
            "商戶名稱",
            "商戶號",
            "幣種",
            "實際出款",
            "手續費",
            "代理金流費",
            "玩家銀行名稱",
            "玩家銀行卡號",
            "玩家銀行開戶行地址",
            "玩家錢包地址",
            "玩家錢包協議",
            "玩家錢包備註名",
            "交易所錢包地址",
            "交易所錢包名稱",
            "交易所錢包備註",
            "VIP等級",
            "操作端",
            "審核分配員",
            "審核分配備註",
            "審核分配時間",
            "出款審核員",
            "出款審核備註",
            "出款審核時間",
            "出款分配員",
            "出款分配備註",
            "出款分配時間",
            "出款人",
            "出款備註",
            "出款時間",
            // "異常托售處理備註",
            "異常出款備註",
            "請求資訊"
        ));
        reportUpdateDto.setRows(createCsvRowsData(pageVo.getRecords(), timezone, factory));
        reportUpdateDto.setTotalPage(totalPage.intValue());
        reportUpdateDto.setCurrentPage(currentPage.intValue());
        return reportUpdateDto;
    }

    private void makeReport(ReportQryVo qryVo, PageVo<WithdrawVo> pageVo, Long totalPage, Long currentPage, Integer timezone, ReportMaskFactory factory) {
        ReportUpdateDto reportUpdateDto = getReportUpdateDto(qryVo, pageVo, totalPage, currentPage, timezone, factory);
        basicFeignClient.makeReportDocument(reportUpdateDto);
        log.info("[WithdrawSummaryReport], reportUpdateDto:{}", reportUpdateDto);
    }

}
