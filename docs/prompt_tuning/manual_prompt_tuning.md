# 手动提示调整 ⚙️

GraphRAG索引器默认使用一组设计用于广泛知识发现场景的提示。然而，通常需要根据特定用例调整提示。我们提供了一种方法，允许您通过指定自定义提示文件来进行调整，每个提示文件内部都会使用一系列标记替换。

每个提示都可以通过编写纯文本自定义提示文件来覆盖。我们使用 `{token_name}` 形式的标记替换，可用标记的描述如下。

## 索引提示

### 实体/关系提取

[提示源](http://github.com/microsoft/graphrag/blob/main/graphrag/prompts/index/entity_extraction.py)

#### 标记

- **{input_text}** - 要处理的输入文本。
- **{entity_types}** - 实体类型列表。
- **{tuple_delimiter}** - 用于分隔元组内值的分隔符。单个元组用于表示单个实体或关系。
- **{record_delimiter}** - 用于分隔元组实例的分隔符。
- **{completion_delimiter}** - 表示生成完成的标志。

### 总结实体/关系描述

[提示源](http://github.com/microsoft/graphrag/blob/main/graphrag/prompts/index/summarize_descriptions.py)

#### 标记

- **{entity_name}** - 实体名称或关系的源/目标对。
- **{description_list}** - 实体或关系的描述列表。

### 声明提取

[提示源](http://github.com/microsoft/graphrag/blob/main/graphrag/prompts/index/claim_extraction.py)

#### 标记

- **{input_text}** - 要处理的输入文本。
- **{tuple_delimiter}** - 用于分隔元组内值的分隔符。单个元组用于表示单个实体或关系。
- **{record_delimiter}** - 用于分隔元组实例的分隔符。
- **{completion_delimiter}** - 表示生成完成的标志。
- **{entity_specs}** - 实体类型列表。
- **{claim_description}** - 声明应如何呈现的描述。默认值为：“任何可能与信息发现相关的声明或事实。”

有关如何更改此设置的详细信息，请参阅[配置文档](../config/overview.md)。

### 生成社区报告

[提示源](http://github.com/microsoft/graphrag/blob/main/graphrag/prompts/index/community_report.py)

#### 标记

- **{input_text}** - 用于生成报告的输入文本。此文本将包含实体和关系表。

## 查询提示

### 本地搜索

[提示源](http://github.com/microsoft/graphrag/blob/main/graphrag/prompts/query/local_search_system_prompt.py)

#### 标记

- **{response_type}** - 描述响应的格式。我们默认为“多段落”。
- **{context_data}** - GraphRAG索引中的数据表。

### 全局搜索

[映射器提示源](http://github.com/microsoft/graphrag/blob/main/graphrag/prompts/query/global_search_map_system_prompt.py)

[归约器提示源](http://github.com/microsoft/graphrag/blob/main/graphrag/prompts/query/global_search_reduce_system_prompt.py)

[知识提示源](http://github.com/microsoft/graphrag/blob/main/graphrag/prompts/query/global_search_knowledge_system_prompt.py)

全局搜索使用映射/归约方法进行摘要。您可以独立调整这些提示。此搜索还包括调整使用模型训练中获得的通用知识的功能。

#### 标记

- **{response_type}** - 描述响应的格式（仅限归约器）。我们默认为“多段落”。
- **{context_data}** - GraphRAG索引中的数据表。

### 漂移搜索

[提示源](http://github.com/microsoft/graphrag/blob/main/graphrag/prompts/query/drift_search_system_prompt.py)

#### 标记

- **{response_type}** - 描述响应的格式。我们默认为“多段落”。
- **{context_data}** - GraphRAG索引中的数据表。
- **{community_reports}** - 包含在摘要中最相关的社区报告。
- **{query}** - 注入到上下文中的查询文本。