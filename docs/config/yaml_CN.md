# 默认配置模式（使用 YAML/JSON）

默认配置模式可以通过在数据项目根目录中使用 `settings.yml` 或 `settings.json` 文件进行配置。如果存在 `.env` 文件与此配置文件一起，则会加载该文件，其中定义的环境变量可用于配置文档中的令牌替换，语法为 `${ENV_VAR}`。我们默认在 `graphrag init` 中使用 YML 初始化，但您也可以根据需要使用等效的 JSON 格式。

许多配置值都有默认值。这里不再赘述，请直接参阅[代码中的常量](https://github.com/microsoft/graphrag/blob/main/graphrag/config/defaults.py)。

例如：

```
# .env
GRAPHRAG_API_KEY=some_api_key

# settings.yml
llm: 
  api_key: ${GRAPHRAG_API_KEY}
```

# 配置部分

## 语言模型设置

### models

这是一个模型配置的字典。字典的键用于在需要模型实例时引用该配置。通过这种方式，您可以根据需要指定多个不同的模型，并在工作流程步骤中分别引用它们。

例如：
```yml
models:
  default_chat_model:
    api_key: ${GRAPHRAG_API_KEY}
    type: openai_chat
    model: gpt-4o
    model_supports_json: true
  default_embedding_model:
    api_key: ${GRAPHRAG_API_KEY}
    type: openai_embedding
    model: text-embedding-ada-002
```

#### Fields

- `api_key` **字符串** - 要使用的 OpenAI API 密钥。
- `auth_type` **api_key|managed_identity** - 指示请求的认证方式。
- `type` **openai_chat|azure_openai_chat|openai_embedding|azure_openai_embedding|mock_chat|mock_embeddings** - 要使用的语言模型类型。
- `model` **字符串** - 模型名称。
- `encoding_model` **字符串** - 要使用的文本编码模型。默认使用与语言模型对齐的编码模型（即，如果未设置，则从 tiktoken 获取）。
- `api_base` **字符串** - 要使用的 API 基础 URL。
- `api_version` **字符串** - API 版本。
- `deployment_name` **字符串** - 要使用的部署名称（Azure）。
- `organization` **字符串** - 客户端组织。
- `proxy` **字符串** - 要使用的代理 URL。
- `audience` **字符串** - （仅限 Azure OpenAI）请求托管身份令牌的目标 Azure 资源/服务的 URI。如果未定义 `api_key`，则使用。默认=`https://cognitiveservices.azure.com/.default`
- `model_supports_json` **布尔值** - 模型是否支持 JSON 模式输出。
- `request_timeout` **浮点数** - 每个请求的超时时间。
- `tokens_per_minute` **整数** - 设置每分钟令牌的漏斗限制。
- `requests_per_minute` **整数** - 设置每分钟请求的漏斗限制。
- `retry_strategy` **字符串** - 要使用的重试策略，默认是 “native”，使用 OpenAI SDK 内置的策略。其他允许值包括 “exponential_backoff”、“random_wait” 和 “incremental_wait”。
- `max_retries` **整数** - 最大重试次数。
- `max_retry_wait` **浮点数** - 最大回退时间。
- `concurrent_requests` **整数** - 允许的并发请求数。
- `async_mode` **asyncio|threaded** - 要使用的异步模式。可以是 `asyncio` 或 `threaded`。
- `responses` **字符串列表** - 如果模型类型为模拟类型，则这是返回的响应字符串列表。
- `n` **整数** - 要生成的完成数量。
- `max_tokens` **整数** - 最大输出令牌数。o 系列模型不可用。
- `temperature` **浮点数** - 要使用的温度。o 系列模型不可用。
- `top_p` **浮点数** - 要使用的 top-p 值。o 系列模型不可用。
- `frequency_penalty` **浮点数** - 令牌生成的频率惩罚。o 系列模型不可用。
- `presence_penalty` **浮点数** - 令牌生成的存在惩罚。o 系列模型不可用。
- `max_completion_tokens` **整数** - 聊天完成的令牌消耗最大数量。必须足够大以包括模型“推理”的未知数量。仅限 o 系列模型。
- `reasoning_effort` **低|中|高** - 模型在推理响应时花费的“思考”量。仅限 o 系列模型。

## Input Files and Chunking


### 输入

我们的管道可以从输入文件夹中摄取 `.csv`、`.txt` 或 `.json` 数据。有关更多细节和示例，请参阅[输入页面](../index/inputs.md)。

#### 字段

- `type` **文件|blob** - 要使用的输入类型。默认=`file`
- `file_type` **text|csv|json** - 要加载的输入数据类型。默认=`text`
- `base_dir` **字符串** - 读取输入的基准目录，相对于根目录。
- `connection_string` **字符串** - （仅限 blob）Azure 存储连接字符串。
- `storage_account_blob_url` **字符串** - 要使用的存储账户 blob URL。
- `container_name` **字符串** - （仅限 blob）Azure 存储容器名称。
- `encoding` **字符串** - 输入文件的编码。默认=`utf-8`
- `file_pattern` **字符串** - 匹配输入文件的正则表达式。默认根据指定的 `file_type` 为 `.*\.csv$`、`.+\.txt$` 或 `.*\.json$`，但可以根据需要自定义。
- `file_filter` **字典** - 键/值对过滤器。默认=None。
- `text_column` **字符串** - （仅限 CSV/JSON）文本列名称。如果未设置，期望有一个名为 `text` 的列。
- `title_column` **字符串** - （仅限 CSV/JSON）标题列名称，如果未设置，将使用文件名。
- `metadata` **字符串列表** - （仅限 CSV/JSON）要保留的额外文档属性字段。

### 分块

这些设置配置如何将文档解析为文本块。这是必要的，因为非常大的文档可能无法适应单个上下文窗口，图提取的准确性也可以调整。另请注意输入文档配置中的 `metadata` 设置，它会将文档元数据复制到每个分块中。

#### 字段

- `size` **整数** - 最大分块大小（以令牌计）。
- `overlap` **整数** - 分块重叠（以令牌计）。
- `group_by_columns` **字符串列表** - 在分块之前按这些字段对文档进行分组。
- `strategy` **字符串**[tokens|sentences] - 如何分块文本。
- `encoding_model` **字符串** - 用于按令牌边界分割的文本编码模型。
- `prepend_metadata` **布尔值** - 确定是否在每个分块的开头添加元数据值。默认=`False`。
- `chunk_size_includes_metadata` **布尔值** - 指定分块大小计算是否应包括元数据令牌。默认=`False`。

## Outputs and Storage

### 输出

本部分控制管道用于导出输出表的存储机制。

#### 字段

- `type` **file|memory|blob|cosmosdb** - 要使用的存储类型。默认=`file`
- `base_dir` **字符串** - 写入输出工件的基准目录，相对于根目录。
- `connection_string` **字符串** - （仅限 blob/cosmosdb）Azure 存储连接字符串。
- `container_name` **字符串** - （仅限 blob/cosmosdb）Azure 存储容器名称。
- `storage_account_blob_url` **字符串** - （仅限 blob）要使用的存储账户 blob URL。
- `cosmosdb_account_blob_url` **字符串** - （仅限 cosmosdb）CosmosDB 账户 blob URL。

### 更新索引输出

本部分定义了用于增量索引的辅助存储位置，以保留原始输出。

#### 字段

- `type` **file|memory|blob|cosmosdb** - 要使用的存储类型。默认=`file`
- `base_dir` **字符串** - 写入输出工件的基准目录，相对于根目录。
- `connection_string` **字符串** - （仅限 blob/cosmosdb）Azure 存储连接字符串。
- `container_name` **字符串** - （仅限 blob/cosmosdb）Azure 存储容器名称。
- `storage_account_blob_url` **字符串** - （仅限 blob）要使用的存储账户 blob URL。
- `cosmosdb_account_blob_url` **字符串** - （仅限 cosmosdb）CosmosDB 账户 blob URL。

### 缓存

本部分控制管道使用的缓存机制。用于缓存 LLM 调用结果，以便在重新运行索引过程时提高性能。

#### 字段

- `type` **file|memory|blob|cosmosdb** - 要使用的存储类型。默认=`file`
- `base_dir` **字符串** - 写入输出工件的基准目录，相对于根目录。
- `connection_string` **字符串** - （仅限 blob/cosmosdb）Azure 存储连接字符串。
- `container_name` **字符串** - （仅限 blob/cosmosdb）Azure 存储容器名称。
- `storage_account_blob_url` **字符串** - （仅限 blob）要使用的存储账户 blob URL。
- `cosmosdb_account_blob_url` **字符串** - （仅限 cosmosdb）CosmosDB 账户 blob URL。

### 报告

本部分控制管道用于常见事件和错误消息的报告机制。默认是将报告写入输出目录中的文件。但是，您也可以选择将报告写入控制台或 Azure Blob 存储容器。

#### 字段

- `type` **file|console|blob** - 要使用的报告类型。默认=`file`
- `base_dir` **字符串** - 写入报告的基准目录，相对于根目录。
- `connection_string` **字符串** - （仅限 blob）Azure 存储连接字符串。
- `container_name` **字符串** - （仅限 blob）Azure 存储容器名称。
- `storage_account_blob_url` **字符串** - 要使用的存储账户 blob URL。

### 向量存储

系统所有向量的存储位置。默认配置为 lancedb。这是一个字典，键用于标识单个存储参数（例如，用于文本嵌入）。

#### 字段

- `type` **lancedb|azure_ai_search|cosmosdb** - 向量存储类型。默认=`lancedb`
- `db_uri` **字符串**（仅限 lancedb） - 数据库 URI。默认=`storage.base_dir/lancedb`
- `url` **字符串**（仅限 AI Search） - AI Search 端点
- `api_key` **字符串**（仅限 AI Search，可选） - 要使用的 AI Search API 密钥。
- `audience` **字符串**（仅限 AI Search） - 如果使用托管身份认证，则为托管身份令牌的受众。
- `container_name` **字符串** - 向量容器名称。存储给定数据集摄取的所有索引（表）。默认=`default`
- `database_name` **字符串**（仅限 cosmosdb） - 数据库名称。
- `overwrite` **布尔值**（仅在索引创建时使用） - 如果存在则覆盖集合。默认=`True`

## Workflow Configurations

这些设置控制每个单独的工作流程的执行。

### 工作流程

**字符串列表** - 这是要运行的工作流程名称列表，按顺序执行。GraphRAG 具有内置管道来配置此项，但您可以通过在此指定列表来精确运行您想要的内容。如果您已经完成了部分处理，这将非常有用。

### 嵌入文本

默认情况下，GraphRAG 索引器只会导出查询方法所需的嵌入。但是，模型为所有纯文本字段定义了嵌入，可以通过设置 `target` 和 `names` 字段进行自定义。

支持的嵌入名称包括：

- `text_unit.text`
- `document.text`
- `entity.title`
- `entity.description`
- `relationship.description`
- `community.title`
- `community.summary`
- `community.full_content`

#### 字段

- `model_id` **字符串** - 用于文本嵌入的模型定义名称。
- `vector_store_id` **字符串** - 要写入的向量存储定义名称。
- `batch_size` **整数** - 最大批处理大小。
- `batch_max_tokens` **整数** - 最大批处理令牌数。
- `names` **字符串列表** - 要运行的嵌入名称列表（必须在支持列表中）。

### 提取图

调整基于语言模型的图提取过程。

#### 字段

- `model_id` **字符串** - 用于 API 调用的模型定义名称。
- `prompt` **字符串** - 要使用的提示文件。
- `entity_types` **字符串列表** - 要识别的实体类型。
- `max_gleanings` **整数** - 最大提取周期数。

### 总结描述

#### 字段

- `model_id` **字符串** - 用于 API 调用的模型定义名称。
- `prompt` **字符串** - 要使用的提示文件。
- `max_length` **整数** - 每次总结的最大输出令牌数。
- `max_input_length` **整数** - 用于总结的最大输入令牌数（这将限制为给定实体或关系发送的描述数量）。

### 提取图 NLP

定义基于 NLP 的图提取方法的设置。

#### 字段

- `normalize_edge_weights` **布尔值** - 是否在图构建期间规范化边权重。默认=`True`。
- `text_analyzer` **字典** - NLP 模型的参数。
  - extractor_type **regex_english|syntactic_parser|cfg** - 默认=`regex_english`。
  - model_name **字符串** - NLP 模型名称（基于 SpaCy 的模型）。
  - max_word_length **整数** - 允许的最长单词。默认=`15`。
  - word_delimiter **字符串** - 分割单词的分隔符。默认=' '。
  - include_named_entities **布尔值** - 是否在名词短语中包含命名实体。默认=`True`。
  - exclude_nouns **字符串列表 | None** - 要排除的名词列表。如果为 `None`，则使用内部停用词列表。
  - exclude_entity_tags **字符串列表** - 要忽略的实体标签列表。
  - exclude_pos_tags **字符串列表** - 要忽略的词性标签列表。
  - noun_phrase_tags **字符串列表** - 要忽略的名词短语标签列表。
  - noun_phrase_grammars **字典[字符串, 字符串]** - 模型的名词短语语法（仅限 cfg）。

### 修剪图

手动修剪图的参数。可用于优化图集群的模块化，移除过度连接或稀有节点。

#### 字段

- `min_node_freq` **整数** - 允许的最小节点频率。
- `max_node_freq_std` **浮点数 | None** - 允许的节点频率最大标准差。
- `min_node_degree` **整数** - 允许的最小节点度。
- `max_node_degree_std` **浮点数 | None** - 允许的节点度最大标准差。
- `min_edge_weight_pct` **浮点数** - 允许的最小边权重百分位。
- `remove_ego_nodes` **布尔值** - 移除自我节点。
- `lcc_only` **布尔值** - 仅使用最大连通分量。

### 集群图

这些是用于图的 Leiden 层次聚类以创建社区的设置。

#### 字段

- `max_cluster_size` **整数** - 导出的最大集群大小。
- `use_lcc` **布尔值** - 是否仅使用最大连通分量。
- `seed` **整数** - 如果需要运行结果一致性，提供随机种子。我们提供默认值以保证聚类稳定性。

### 提取声明

#### 字段

- `enabled` **布尔值** - 是否启用声明提取。默认关闭，因为声明提示需要用户调整。
- `model_id` **字符串** - 用于 API 调用的模型定义名称。
- `prompt` **字符串** - 要使用的提示文件。
- `description` **字符串** - 描述我们希望提取的声明类型。
- `max_gleanings` **整数** - 最大提取周期数。

### 社区报告

#### 字段

- `model_id` **字符串** - 用于 API 调用的模型定义名称。
- `prompt` **字符串** - 要使用的提示文件。
- `max_length` **整数** - 每个报告的最大输出令牌数。
- `max_input_length` **整数** - 生成报告时使用的最大输入令牌数。

### 嵌入图

我们使用 node2vec 嵌入图。这主要用于可视化，因此默认不启用。

#### 字段

- `enabled` **布尔值** - 是否启用图嵌入。
- `dimensions` **整数** - 产生的向量维度数。
- `num_walks` **整数** - node2vec 步行次数。
- `walk_length` **整数** - node2vec 步行长度。
- `window_size` **整数** - node2vec 窗口大小。
- `iterations` **整数** - node2vec 迭代次数。
- `random_seed` **整数** - node2vec 随机种子。
- `strategy` **字典** - 完全覆盖嵌入图策略。

### UMAP

指示是否运行 UMAP 降维。用于为每个图节点提供 x/y 坐标，适合可视化。如果未启用，节点将获得 0/0 x/y 坐标。如果启用，您*必须*同时启用图嵌入。

#### 字段

- `enabled` **布尔值** - 是否启用 UMAP 布局。

### 快照

#### 字段

- `embeddings` **布尔值** - 将嵌入快照导出到 parquet。
- `graphml` **布尔值** - 将图快照导出到 GraphML。

## Query

### 本地搜索

#### 字段

- `chat_model_id` **字符串** - 用于聊天完成调用的模型定义名称。
- `embedding_model_id` **字符串** - 用于嵌入调用的模型定义名称。
- `prompt` **字符串** - 要使用的提示文件。
- `text_unit_prop` **浮点数** - 文本单位比例。
- `community_prop` **浮点数** - 社区比例。
- `conversation_history_max_turns` **整数** - 对话历史最大轮次。
- `top_k_entities` **整数** - 映射的顶级 k 实体。
- `top_k_relationships` **整数** - 映射的顶级 k 关系。
- `max_context_tokens` **整数** - 构建请求上下文的最大令牌数。

### 全局搜索

#### 字段

- `chat_model_id` **字符串** - 用于聊天完成调用的模型定义名称。
- `map_prompt` **字符串** - 要使用的映射器提示文件。
- `reduce_prompt` **字符串** - 要使用的归约器提示文件。
- `knowledge_prompt` **字符串** - 要使用的知识提示文件。
- `map_prompt` **字符串 | None** - 全局搜索映射器提示。
- `reduce_prompt` **字符串 | None** - 全局搜索归约器。
- `knowledge_prompt` **字符串 | None** - 全局搜索通用提示。
- `max_context_tokens` **整数** - 创建的最大上下文大小（以令牌计）。
- `data_max_tokens` **整数** - 从归约响应构建最终响应的最大令牌数。
- `map_max_length` **整数** - 映射响应的最大请求长度（以单词计）。
- `reduce_max_length` **整数** - 归约响应的最大请求长度（以单词计）。
- `dynamic_search_threshold` **整数** - 包含社区报告的评级阈值。
- `dynamic_search_keep_parent` **布尔值** - 如果任何子社区相关，则保留父社区。
- `dynamic_search_num_repeats` **整数** - 对同一社区报告评级的次数。
- `dynamic_search_use_summary` **布尔值** - 使用社区摘要而非完整内容。
- `dynamic_search_max_level` **整数** - 如果处理的社区均不相关，则考虑的社区层次最大级别。

### drift_search

#### 字段

- `chat_model_id` **字符串** - 用于聊天完成调用的模型定义名称。
- `embedding_model_id` **字符串** - 用于嵌入调用的模型定义名称。
- `prompt` **字符串** - 要使用的提示文件。
- `reduce_prompt` **字符串** - 要使用的归约器提示文件。
- `data_max_tokens` **整数** - 数据 LLM 最大令牌数。
- `reduce_max_tokens` **整数** - 归约阶段的最大令牌数。仅用于非 o 系列模型。
- `reduce_max_completion_tokens` **整数** - 归约阶段的最大令牌数。仅用于 o 系列模型。
- `concurrency` **整数** - 并发请求数。
- `drift_k_followups` **整数** - 检索的顶级全局结果数。
- `primer_folds` **整数** - 搜索启动的折叠数。
- `primer_llm_max_tokens` **整数** - 启动中 LLM 的最大令牌数。
- `n_depth` **整数** - 漂移搜索步骤数。
- `local_search_text_unit_prop` **浮点数** - 搜索中分配给文本单位的比例。
- `local_search_community_prop` **浮点数** - 搜索中分配给社区属性的比例。
- `local_search_top_k_mapped_entities` **整数** - 本地搜索中映射的顶级 K 实体数。
- `local_search_top_k_relationships` **整数** - 本地搜索中映射的顶级 K 关系数。
- `local_search_max_data_tokens` **整数** - 本地搜索的最大上下文大小（以令牌计）。
- `local_search_temperature` **浮点数** - 本地搜索中用于令牌生成的温度。
- `local_search_top_p` **浮点数** - 本地搜索中用于令牌生成的 top-p 值。
- `local_search_n` **整数** - 本地搜索中生成的完成数量。
- `local_search_llm_max_gen_tokens` **整数** - 本地搜索中 LLM 生成的最大令牌数。仅用于非 o 系列模型。
- `local_search_llm_max_gen_completion_tokens` **整数** - 本地搜索中 LLM 生成的最大令牌数。仅用于 o 系列模型。

### 基本搜索

#### 字段

- `chat_model_id` **字符串** - 用于聊天完成调用的模型定义名称。
- `embedding_model_id` **字符串** - 用于嵌入调用的模型定义名称。
- `prompt` **字符串** - 要使用的提示文件。
- `k` **整数 | None** - 从向量存储中检索的文本单位数，用于上下文构建。
