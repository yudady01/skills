// ====================================================================
// 複雜報表處理器模板
// 適用條件：有子單 OR 需要隱碼處理
// ====================================================================
package ${HANDLER_IMPL_PACKAGE};

import com.fasterxml.jackson.databind.ObjectMapper;
import ${REPORT_TYPE_IMPORT};
import ${BASIC_FEIGN_CLIENT_IMPORT};
import ${DATA_SOURCE_IMPORT};
import ${HANDLER_INTERFACE_IMPORT};
import ${REPORT_UPDATE_DTO_IMPORT};
import ${REPORT_QRY_VO_IMPORT};
import ${QUERY_DTO_IMPORT};
import ${RESPONSE_VO_IMPORT};
import ${PAGE_VO_IMPORT};
import ${MASK_FACTORY_IMPORT}; // 隱碼處理
import java.util.ArrayList;
import java.util.List;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Component;

import static ${HEADER_KEY_IMPORT}.H_KEY_LANGUAGE;
import static ${HEADER_KEY_IMPORT}.H_KEY_CURRENCY;
import static ${REPORT_CONVERT_UTILS_IMPORT}.convertString;

/**
 * ${REPORT_TYPE_DESC}
 */
@Slf4j
@Component
@RequiredArgsConstructor
public class $ {
    HANDLER_CLASS}implements DownloadReportHandler{

    private static final long MAX_SIZE = 500L;
    private static final long START_PAGE = 1L;

    private final ${BASIC_FEIGN_CLIENT_NAME}basicFeignClient;private final ${DATA_SOURCE_CLASS}${DATA_SOURCE_FIELD};
    private final ObjectMapper mapper;

    @Override
    public ReportType type() {
        return ReportType.${REPORT_TYPE_ENUM};
    }

    @Override
    public void handle(ReportQryVo qryVo) {
        log.info("[${REPORT_TYPE_ENUM}], START");
        
        ${QUERY_DTO_CLASS} queryDto = mapper.convertValue(
            qryVo.getSearchParam(), ${QUERY_DTO_CLASS}.class);
        Integer timezone = qryVo.getTimezone();
        String language = String.valueOf(qryVo.getSearchParam().get(H_KEY_LANGUAGE));
        String currency = String.valueOf(qryVo.getSearchParam().get(H_KEY_CURRENCY));
        
        queryDto.setPage(START_PAGE);
        queryDto.setSize(MAX_SIZE);

        // 初始化隱碼處理器
        ReportMaskFactory factory = ReportMaskFactory.get(mapper, qryVo.getUnmaskAuths());

        long current;
        long pages;
        PageVo<${RESPONSE_VO_CLASS}> pageVo;
        
        try {
            do {
                // TODO: 根據實際 API 調整參數
                pageVo = ${DATA_SOURCE_FIELD}.${API_METHOD}(language, queryDto, currency);
                makeReport(qryVo, pageVo, pageVo.getPages(), pageVo.getCurrent(), timezone, factory);

                current = pageVo.getCurrent() + 1;
                queryDto.setPage(current);
                pages = pageVo.getPages();
            } while (!pageVo.getRecords().isEmpty() && current <= pages);
        } finally {
            // 清理隱碼處理器的 ThreadLocal
            factory.finish();
        }

        log.info("[${REPORT_TYPE_ENUM}], END");
    }

    private List<List<String>> createCsvRowsData(List<${RESPONSE_VO_CLASS}>records,

    Integer timezone,
            ReportMaskFactory factory)
    {
        List<List<String>> rows = new ArrayList<>();

        for (${RESPONSE_VO_CLASS} record : records) {
            // 應用隱碼處理
            factory.check(record);
            
            List<String> row = new ArrayList<>();
            
            ${CSV_ROWS}

            rows.add(row);
            
            // 如果有子單，處理子單資料
            ${SUB_RECORDS_PROCESSING}
        }
        return rows;
    }

    private void makeReport(ReportQryVo qryVo, PageVo<${RESPONSE_VO_CLASS}>pageVo,

    Long totalPage, Long currentPage,
    Integer timezone,
            ReportMaskFactory factory)
    {
        ReportUpdateDto dto = new ReportUpdateDto();
        dto.setId(qryVo.getId());
        dto.setReportExportType("CSV");
        dto.setTitles(List.of(${CSV_TITLES}));
        dto.setRows(createCsvRowsData(pageVo.getRecords(), timezone, factory));
        dto.setTotalPage(totalPage.intValue());
        dto.setCurrentPage(currentPage.intValue());
        
        basicFeignClient.makeReportDocument(dto);
        log.info("[${HANDLER_CLASS}], dto:{}", dto);
    }
}
