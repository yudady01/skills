---
description: 基于 Context7 的智能文档检索命令，支持 Spring Boot + Dubbo 微服务开发文档的语义搜索
allowed-tools: [Read, Write, Edit, Glob, Grep, Bash, TodoWrite, Task]
---

# 智能文档检索命令

基于 Context7 MCP 服务器的智能文档检索功能，为 Spring Boot + Dubbo 微服务开发提供精准的文档支持。

## 功能特性

### 🔍 多维度搜索
- **语义搜索** - 理解查询意图，找到相关内容
- **关键词搜索** - 精确匹配特定术语
- **分类搜索** - 按文档类型和主题筛选
- **范围搜索** - 内置文档 vs 用户文档

### 📚 丰富的文档源
- **企业级指南** - 4,512+ 行权威开发指南
- **最佳实践** - 编码规范、架构原则
- **配置示例** - 详细的配置模板
- **问题解决方案** - 常见问题和解决方法

## 使用方法

### 基础搜索
```bash
# 搜索特定主题
/docs-search "Spring Boot auto configuration"

# 搜索配置相关
/docs-search "Dubbo 超时配置"

# 搜索最佳实践
/docs-search "微服务架构设计最佳实践"
```

### 高级搜索
```bash
# 按范围搜索
/docs-search "JWT 认证" --scope=builtin
/docs-search "项目设计文档" --scope=user

# 限制结果数量
/docs-search "Redis 缓存配置" --limit=3
```

## 集成场景

### 1. 开发时文档查询
在实现功能过程中快速查找相关文档：
```bash
# 实现用户认证时
/docs-search "Spring Security JWT 配置"

# 性能优化时
/docs-search "数据库查询优化"
```

### 2. 问题诊断
遇到问题时快速查找解决方案：
```bash
# 服务调用超时
/docs-search "Dubbo 调用超时解决"

# 数据库连接问题
/docs-search "数据库连接池配置优化"
```

### 3. 学习和培训
新团队成员学习最佳实践：
```bash
# 学习微服务设计
/docs-search "微服务拆分原则"

# 学习编码规范
/docs-search "Java 编码最佳实践"
```

## Context7 集成

Context7 提供以下核心工具：

### search_documents
搜索文档内容，支持：
- 语义检索
- 关键词匹配
- 结果排序和过滤

### index_document
索引用户文档，支持：
- Markdown、PDF、HTML、文本格式
- 自动分类和标签
- 向量化存储

### get_document_summary
获取文档详细信息：
- 文档元数据
- 分块统计
- 更新时间

### list_documents
浏览已索引文档：
- 按类型筛选
- 更新时间排序
- 格式统计

## 技术特性

- **响应时间 < 5秒** - 满足开发场景性能要求
- **智能缓存** - 常用查询结果缓存
- **增量索引** - 只处理变更的文档
- **异步处理** - 支持并发文档处理