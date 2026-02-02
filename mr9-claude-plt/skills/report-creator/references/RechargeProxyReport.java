package com.galaxy.handler.downloadReportHanlder.impl;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.galaxy.enumeration.basics.ReportType;
import com.galaxy.enumeration.fund.RechargeStatusEnum;
import com.galaxy.feign.client.basic.BasicFeignClient;
import com.galaxy.feign.client.proxy.ProxyFeignClient;
import com.galaxy.handler.downloadReportHanlder.DownloadReportHandler;
import com.galaxy.model.basic.dto.ReportUpdateDto;
import com.galaxy.model.basic.vo.ReportQryVo;
import com.galaxy.model.fund.dto.ProxyBalanceRecordQueryPageDto;
import com.galaxy.model.fund.vo.ProxyBalanceRecordVo;
import com.galaxy.module.model.vo.PageVo;
import java.util.ArrayList;
import java.util.List;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Component;


import static com.galaxy.module.constant.HeaderKey.H_KEY_LANGUAGE;
import static com.galaxy.utils.ReportConvertUtils.convertString;

/**
 * @author hardy
 */
@Slf4j
@Component
@RequiredArgsConstructor
public class RechargeProxyReport implements DownloadReportHandler {

    private final BasicFeignClient basicFeignClient;
    private final ProxyFeignClient proxyFeignClient;
    private final static long MAX_SIZE = 500L;
    private final static long START_PAGE = 1L;
    private final ObjectMapper mapper;

    @Override
    public ReportType type() {
        return ReportType.PLT_REPORT_RECHARGE_PROXY_DOWNLOAD;
    }

    @Override
    public void handle(ReportQryVo qryVo) {
        log.info("[PLT_REPORT_RECHARGE_PROXY_DOWNLOAD], START");
        ProxyBalanceRecordQueryPageDto queryDto = mapper.convertValue(qryVo.getSearchParam(), ProxyBalanceRecordQueryPageDto.class);
        Integer timezone = qryVo.getTimezone();
        String language = String.valueOf(qryVo.getSearchParam().get(H_KEY_LANGUAGE));
        log.info("[RechargeProxyReport], queryDto:{} ,language={} ", queryDto, language);
        queryDto.setPage(START_PAGE);
        queryDto.setSize(MAX_SIZE);

        long current;
        long pages;
        PageVo<ProxyBalanceRecordVo> pageVo;
        do {
            pageVo = proxyFeignClient.proxyReplaceList(language, queryDto).getData();
            makeReport(qryVo, pageVo, pageVo.getPages(), pageVo.getCurrent(), timezone);

            current = pageVo.getCurrent() + 1;
            queryDto.setPage(current);

            pages = pageVo.getPages();
        } while (!pageVo.getRecords().isEmpty() && current <= pages);

        log.info("[PLT_REPORT_RECHARGE_PROXY_DOWNLOAD], END");
    }

    private List<List<String>> createCsvRowsData(List<ProxyBalanceRecordVo> records, Integer timezone) {
        List<List<String>> rows = new ArrayList<>();

        for (ProxyBalanceRecordVo record : records) {
            List<String> row = new ArrayList<>();

            // 訂單號
            row.add(record.getTradeId());
            // 帳戶名
            row.add(record.getUsername());
            // 代理
            row.add(record.getProxy());
            // 幣種
            row.add(record.getCurrency());
            // 充值金額
            row.add(convertString(record.getAmount()));
            // 充值時間
            row.add(convertString(record.getCreateTime(), timezone, "--"));
            // 支付狀態
            row.add(RechargeStatusEnum.valueOf(record.getStatus()).getDescription());
            // 備註
            row.add(record.getRemark());

            rows.add(row);
        }
        return rows;
    }

    private ReportUpdateDto getReportUpdateDto(ReportQryVo qryVo, PageVo<ProxyBalanceRecordVo> pageVo, Long totalPage, Long currentPage, Integer timezone) {
        ReportUpdateDto reportUpdateDto = new ReportUpdateDto();
        reportUpdateDto.setId(qryVo.getId());
        reportUpdateDto.setReportExportType("CSV");
        reportUpdateDto.setTitles(
            List.of("訂單號",
                    "帳戶名",
                    "代理",
                    "幣種",
                    "充值金額",
                    "充值時間",
                    "支付狀態",
                    "備註")
        );
        reportUpdateDto.setRows(createCsvRowsData(pageVo.getRecords(), timezone));
        reportUpdateDto.setTotalPage(totalPage.intValue());
        reportUpdateDto.setCurrentPage(currentPage.intValue());
        return reportUpdateDto;
    }

    private void makeReport(ReportQryVo qryVo, PageVo<ProxyBalanceRecordVo> pageVo, Long totalPage, Long currentPage, Integer timezone) {
        ReportUpdateDto reportUpdateDto = getReportUpdateDto(qryVo, pageVo, totalPage, currentPage, timezone);
        basicFeignClient.makeReportDocument(reportUpdateDto);
        log.info("[RechargeProxyReport], reportUpdateDto:{}", reportUpdateDto);
    }

}
