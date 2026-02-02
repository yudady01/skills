// ====================================================================
// 簡單報表處理器模板
// 適用條件：單一 VO、無子單、無隱碼需求
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
import java.util.ArrayList;
import java.util.List;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Component;

import static ${REPORT_CONVERT_UTILS_IMPORT}.convertString;
// 如果需要從 searchParam 提取參數，取消以下註釋：
// import static ${HEADER_KEY_IMPORT}.H_KEY_LANGUAGE;
// import static ${HEADER_KEY_IMPORT}.H_KEY_CURRENCY;

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
        // 如果需要從 searchParam 提取參數：
        // String language = String.valueOf(qryVo.getSearchParam().get(H_KEY_LANGUAGE));
        // String currency = String.valueOf(qryVo.getSearchParam().get(H_KEY_CURRENCY));
        
        queryDto.setPage(START_PAGE);
        queryDto.setSize(MAX_SIZE);

        long current;
        long pages;
        PageVo<${RESPONSE_VO_CLASS}> pageVo;
        
        do {
            // TODO: 根據實際 API 調整參數
            pageVo = ${DATA_SOURCE_FIELD}.${API_METHOD}(queryDto).getData();
            makeReport(qryVo, pageVo, pageVo.getPages(), pageVo.getCurrent(), timezone);

            current = pageVo.getCurrent() + 1;
            queryDto.setPage(current);
            pages = pageVo.getPages();
        } while (!pageVo.getRecords().isEmpty() && current <= pages);

        log.info("[${REPORT_TYPE_ENUM}], END");
    }

    private List<List<String>> createCsvRowsData(List<${RESPONSE_VO_CLASS}>records,

    Integer timezone)
    {
        List<List<String>> rows = new ArrayList<>();

        for (${RESPONSE_VO_CLASS} record : records) {
            List<String> row = new ArrayList<>();
            
            ${CSV_ROWS}

            rows.add(row);
        }
        return rows;
    }

    private void makeReport(ReportQryVo qryVo, PageVo<${RESPONSE_VO_CLASS}>pageVo,

    Long totalPage, Long currentPage,
    Integer timezone)
    {
        ReportUpdateDto dto = new ReportUpdateDto();
        dto.setId(qryVo.getId());
        dto.setReportExportType("CSV");
        dto.setTitles(List.of(${CSV_TITLES}));
        dto.setRows(createCsvRowsData(pageVo.getRecords(), timezone));
        dto.setTotalPage(totalPage.intValue());
        dto.setCurrentPage(currentPage.intValue());
        
        basicFeignClient.makeReportDocument(dto);
        log.info("[${HANDLER_CLASS}], dto:{}", dto);
    }
}
