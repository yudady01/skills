---
description: 查詢 ot888_user_daily_report Elasticsearch 索引資料
---

# ot888_user_daily_report ES 查詢技能

此技能用於查詢和分析 `ot888_user_daily_report` Elasticsearch 索引中的用戶日報表資料。

## 環境配置

- **Elasticsearch URL**: `https://ot888-sit-elastic-cloud-8-18-1.es.ap-northeast-1.aws.found.io`
- **索引名稱**: `ot888_user_daily_report`
- **認證**: Basic Auth (`sit_developer:sit_developer_elastic_cloud`)

## 常用查詢範本

### 1. 查看索引 Mapping

```bash
curl -s --location --request GET 'https://ot888-sit-elastic-cloud-8-18-1.es.ap-northeast-1.aws.found.io/ot888_user_daily_report/_mapping' \
--header 'Authorization: Basic c2l0X2RldmVsb3BlcjpzaXRfZGV2ZWxvcGVyX2VsYXN0aWNfY2xvdWQ=' \
--header 'Content-Type: application/json' | jq .
```

### 2. 查詢特定欄位的值分佈

```bash
curl -s --location --request POST 'https://ot888-sit-elastic-cloud-8-18-1.es.ap-northeast-1.aws.found.io/ot888_user_daily_report/_search' \
--header 'Authorization: Basic c2l0X2RldmVsb3BlcjpzaXRfZGV2ZWxvcGVyX2VsYXN0aWNfY2xvdWQ=' \
--header 'Content-Type: application/json' \
--data-raw '{
  "size": 0,
  "aggs": {
    "field_stats": {
      "stats": {
        "field": "FIELD_NAME"
      }
    }
  }
}' | jq .
```

### 3. 查詢符合條件的文檔數量

```bash
curl -s --location --request POST 'https://ot888-sit-elastic-cloud-8-18-1.es.ap-northeast-1.aws.found.io/ot888_user_daily_report/_count' \
--header 'Authorization: Basic c2l0X2RldmVsb3BlcjpzaXRfZGV2ZWxvcGVyX2VsYXN0aWNfY2xvdWQ=' \
--header 'Content-Type: application/json' \
--data-raw '{
  "query": {
    "range": {
      "FIELD_NAME": {
        "gt": 0
      }
    }
  }
}' | jq .
```

### 4. 查詢樣本資料

```bash
curl -s --location --request POST 'https://ot888-sit-elastic-cloud-8-18-1.es.ap-northeast-1.aws.found.io/ot888_user_daily_report/_search' \
--header 'Authorization: Basic c2l0X2RldmVsb3BlcjpzaXRfZGV2ZWxvcGVyX2VsYXN0aWNfY2xvdWQ=' \
--header 'Content-Type: application/json' \
--data-raw '{
  "size": 10,
  "_source": ["user_id", "username", "day", "FIELD_NAME"],
  "query": {
    "range": {
      "FIELD_NAME": {
        "lt": 0
      }
    }
  }
}' | jq .
```

### 5. 日期範圍查詢

```bash
curl -s --location --request POST 'https://ot888-sit-elastic-cloud-8-18-1.es.ap-northeast-1.aws.found.io/ot888_user_daily_report/_search' \
--header 'Authorization: Basic c2l0X2RldmVsb3BlcjpzaXRfZGV2ZWxvcGVyX2VsYXN0aWNfY2xvdWQ=' \
--header 'Content-Type: application/json' \
--data-raw '{
  "size": 10,
  "query": {
    "bool": {
      "filter": [
        {
          "range": {
            "day": {
              "gte": "2026-01-01T00:00:00Z",
              "lte": "2026-01-15T23:59:59Z"
            }
          }
        }
      ]
    }
  }
}' | jq .
```

### 6. 聚合查詢 - 統計不重複用戶數

```bash
curl -s --location --request POST 'https://ot888-sit-elastic-cloud-8-18-1.es.ap-northeast-1.aws.found.io/ot888_user_daily_report/_search' \
--header 'Authorization: Basic c2l0X2RldmVsb3BlcjpzaXRfZGV2ZWxvcGVyX2VsYXN0aWNfY2xvdWQ=' \
--header 'Content-Type: application/json' \
--data-raw '{
  "size": 0,
  "query": {
    "bool": {
      "should": [
        { "range": { "withdraw_exchange_total": { "lt": 0 } } },
        { "range": { "add_user_withdraw_total": { "gt": 0 } } }
      ],
      "minimum_should_match": 1
    }
  },
  "aggs": {
    "distinct_users": {
      "cardinality": {
        "field": "user_id"
      }
    }
  }
}' | jq .
```

## 關鍵欄位說明

| 欄位名稱 | 類型 | 說明 | 備註 |
|---------|------|------|------|
| `user_id` | keyword | 用戶 ID | |
| `username` | keyword | 用戶帳號 | |
| `day` | date | 報表日期 | 格式: date_time |
| `currency` | keyword | 幣別 | |
| `withdraw_exchange_total` | double | 託售金額 | **負數** |
| `withdraw_exchange_count` | integer | 託售次數 | |
| `add_user_withdraw_total` | double | 加幣_託售補單 | 正數 |
| `add_user_withdraw_count` | integer | 加幣_託售補單次數 | |
| `dis_user_withdraw_total` | double | 減幣_託售補單 | |
| `dis_user_withdraw_count` | integer | 減幣_託售補單次數 | |
| `recharge_exchange_total` | double | 儲值金額 | 正數 |
| `recharge_exchange_count` | integer | 儲值次數 | |
| `add_recharge_total` | double | 儲值補分 | |
| `dis_recharge_total` | double | 儲值減分 | |
| `bet_total` | double | 投注總額 | |
| `valid_bet_total` | double | 有效投注金額 | |
| `profit_total` | double | 公司輸贏總金額 | |
| `is_bet` | integer | 是否有投注 | 0:否 1:是 |
| `is_recharge_exchange` | integer | 是否有儲值 | 0:否 1:是 |
| `is_withdraw_exchange` | integer | 是否有託售 | 0:否 1:是 |

## 重要業務邏輯

### 託售人數計算
託售人數 = 有 `withdraw_exchange_total < 0` **或** `add_user_withdraw_total > 0` 的不重複用戶數

```java
subAggregations.put(WITHDRAW_EXCHANGE_MEMBERS, Aggregation.of(a -> a
    .filter(f -> f.bool(b -> b
        .should(s -> s.range(r -> r.field(WITHDRAW_EXCHANGE_TOTAL).lt(JsonData.of(0))))
        .should(s -> s.range(r -> r.field(ADD_USER_WITHDRAW_TOTAL).gt(JsonData.of(0))))
        .minimumShouldMatch("1")))
    .aggregations(Map.of(
        DISTINCT_USERS, Aggregation.of(agg -> agg.cardinality(c -> c.field(USER_ID)))))));
```

### 儲值人數計算
儲值人數 = 有 `recharge_exchange_total > 0` **或** `add_recharge_total > 0` 的不重複用戶數

```java
subAggregations.put(RECHARGE_EXCHANGE_MEMBERS, Aggregation.of(a -> a
    .filter(f -> f.bool(b -> b
        .should(s -> s.range(r -> r.field(RECHARGE_EXCHANGE_TOTAL).gt(JsonData.of(0))))
        .should(s -> s.range(r -> r.field(ADD_RECHARGE_TOTAL).gt(JsonData.of(0))))
        .minimumShouldMatch("1")))
    .aggregations(Map.of(
        DISTINCT_USERS, Aggregation.of(agg -> agg.cardinality(c -> c.field(USER_ID)))))));
```

## 注意事項

1. **負數欄位**: `withdraw_exchange_total` 在 ES 中儲存為負數，查詢時需使用 `lt(0)` 而非 `gt(0)`
2. **認證資訊**: 使用 Basic Auth，credentials 已編碼在 header 中
3. **索引別名**: Java 代碼中可能使用 `*_user_daily_report_alias` 作為索引別名
