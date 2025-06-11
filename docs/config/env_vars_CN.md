# 默认配置模式（使用环境变量）

从版本 1.3 开始，GraphRAG 不再支持完整的预置环境变量集。相反，我们支持在 [settings.yml 文件](yaml.md) 中使用变量替换，因此您可以指定任何您想要的环境变量。

我们期望并在默认 settings.yml 中包含的唯一标准环境变量是 `GRAPHRAG_API_KEY`。如果您已经使用了许多之前的 GRAPHRAG_* 环境变量，您可以通过在 settings.yml 中使用模板语法插入它们，它们将被采用。

> **以下环境变量的记录是为了帮助迁移，但除非您在 settings.yml 中使用模板语法，否则它们将不会被读取。**

---

### 文本嵌入定制

默认情况下，GraphRAG 索引器只会导出查询方法所需的嵌入。然而，模型为所有纯文本字段定义了嵌入，这些嵌入可以通过将 `GRAPHRAG_EMBEDDING_TARGET` 环境变量设置为 `all` 来生成。

#### 嵌入字段

- `text_unit.text`
- `document.text`
- `entity.title`
- `entity.description`
- `relationship.description`
- `community.title`
- `community.summary`
- `community.full_content`

### 输入数据

我们的管道可以从输入文件夹中摄取 .csv 或 .txt 数据。这些文件可以嵌套在子文件夹中。要配置如何处理输入数据、映射哪些字段以及如何解析时间戳，请查找以下以 `GRAPHRAG_INPUT_` 开头的配置值。通常，基于 CSV 的数据提供最大的自定义可能性。每个 CSV 至少应包含一个 `text` 字段（可以通过环境变量映射），但如果还包含 `title`、`timestamp` 和 `source` 字段会更有帮助。还可以包括额外的字段，这些字段将作为 `Document` 表中的额外字段。

### 基础 LLM 设置

这些是配置 LLM 连接的主要设置。

| 参数                        | 是否必需？                           | 描述                                                                                                                          | 类型  | 默认值        |
| --------------------------- | ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------- | ----- | ------------- |
| `GRAPHRAG_API_KEY`          | **OpenAI 必需，AOAI 可选**           | API 密钥。（注意：`OPENAI_API_KEY` 也用作后备）。如果在使用 AOAI 时未定义，将使用托管身份。                            | `str` | `None`        |
| `GRAPHRAG_API_BASE`         | **AOAI 必需**                        | API 基础 URL                                                                                                                  | `str` | `None`        |
| `GRAPHRAG_API_VERSION`      | **AOAI 必需**                        | AOAI API 版本                                                                                                                 | `str` | `None`        |
| `GRAPHRAG_API_ORGANIZATION` |                                      | AOAI 组织                                                                                                                     | `str` | `None`        |
| `GRAPHRAG_API_PROXY`        |                                      | AOAI 代理                                                                                                                     | `str` | `None`        |

### 文本生成设置

这些设置控制管道使用的文本生成模型。任何具有后备的设置将使用基础 LLM 设置（如果可用）。

| 参数                                              | 是否必需？               | 描述                                                                                 | 类型    | 默认值                 |
| ------------------------------------------------- | ------------------------ | ----------------------------------------------------------------------------------- | ------- | --------------------- |
| `GRAPHRAG_LLM_TYPE`                               | **AOAI 必需**            | LLM 操作类型。可以是 `openai_chat` 或 `azure_openai_chat`                           | `str`   | `openai_chat`         |
| `GRAPHRAG_LLM_DEPLOYMENT_NAME`                    | **AOAI 必需**            | AOAI 模型部署名称                                                                   | `str`   | `None`                |
| `GRAPHRAG_LLM_API_KEY`                            | 是（使用后备）           | API 密钥。如果在使用 AOAI 时未定义，将使用托管身份                                  | `str`   | `None`                |
| `GRAPHRAG_LLM_API_BASE`                           | AOAI（使用后备）         | API 基础 URL                                                                        | `str`   | `None`                |
| `GRAPHRAG_LLM_API_VERSION`                        | AOAI（使用后备）         | AOAI API 版本                                                                       | `str`   | `None`                |
| `GRAPHRAG_LLM_API_ORGANIZATION`                   | AOAI（使用后备）         | AOAI 组织                                                                           | `str`   | `None`                |
| `GRAPHRAG_LLM_API_PROXY`                          |                          | AOAI 代理                                                                           | `str`   | `None`                |
| `GRAPHRAG_LLM_MODEL`                              |                          | LLM 模型                                                                            | `str`   | `gpt-4-turbo-preview` |
| `GRAPHRAG_LLM_MAX_TOKENS`                         |                          | 最大令牌数                                                                          | `int`   | `4000`                |
| `GRAPHRAG_LLM_REQUEST_TIMEOUT`                    |                          | 从聊天客户端等待响应的最大秒数                                                      | `int`   | `180`                 |
| `GRAPHRAG_LLM_MODEL_SUPPORTS_JSON`                |                          | 指示给定模型是否支持 JSON 输出模式。`True` 启用                                     | `str`   | `None`                |
| `GRAPHRAG_LLM_THREAD_COUNT`                       |                          | 用于 LLM 并行化的线程数                                                            | `int`   | 50                    |
| `GRAPHRAG_LLM_THREAD_STAGGER`                     |                          | 启动每个线程之间的等待时间（秒）                                                    | `float` | 0.3                   |
| `GRAPHRAG_LLM_CONCURRENT_REQUESTS`                |                          | 嵌入客户端允许的并发请求数                                                          | `int`   | 25                    |
| `GRAPHRAG_LLM_TOKENS_PER_MINUTE`                  |                          | LLM 客户端每分钟允许的令牌数。0 = 绕过                                             | `int`   | 0                     |
| `GRAPHRAG_LLM_REQUESTS_PER_MINUTE`                |                          | LLM 客户端每分钟允许的请求数。0 = 绕过                                             | `int`   | 0                     |
| `GRAPHRAG_LLM_MAX_RETRIES`                        |                          | 请求失败时尝试的最大重试次数                                                        | `int`   | 10                    |
| `GRAPHRAG_LLM_MAX_RETRY_WAIT`                     |                          | 重试之间等待的最大秒数                                                              | `int`   | 10                    |
| `GRAPHRAG_LLM_SLEEP_ON_RATE_LIMIT_RECOMMENDATION` |                          | 是否在速率限制建议时休眠。（仅限 Azure）                                            | `bool`  | `True`                |
| `GRAPHRAG_LLM_TEMPERATURE`                        |                          | 用于生成的温度                                                                      | `float` | 0                     |
| `GRAPHRAG_LLM_TOP_P`                              |                          | 用于采样的 top_p                                                                    | `float` | 1                     |
| `GRAPHRAG_LLM_N`                                  |                          | 生成的响应数量                                                                      | `int`   | 1                     |

### 文本嵌入设置

这些设置控制管道使用的文本嵌入模型。任何具有后备的设置将使用基础 LLM 设置（如果可用）。

| 参数                                                    | 是否必需？               | 描述                                                                                           | 类型    | 默认值                   |
| ------------------------------------------------------- | ------------------------ | --------------------------------------------------------------------------------------------- | ------- | ------------------------ |
| `GRAPHRAG_EMBEDDING_TYPE`                               | **AOAI 必需**            | 使用的嵌入客户端。可以是 `openai_embedding` 或 `azure_openai_embedding`                       | `str`   | `openai_embedding`       |
| `GRAPHRAG_EMBEDDING_DEPLOYMENT_NAME`                    | **AOAI 必需**            | AOAI 部署名称                                                                                 | `str`   | `None`                   |
| `GRAPHRAG_EMBEDDING_API_KEY`                            | 是（使用后备）           | 用于嵌入客户端的 API 密钥。如果在使用 AOAI 时未定义，将使用托管身份                          | `str`   | `None`                   |
| `GRAPHRAG_EMBEDDING_API_BASE`                           | AOAI（使用后备）         | API 基础 URL                                                                                  | `str`   | `None`                   |
| `GRAPHRAG_EMBEDDING_API_VERSION`                        | AOAI（使用后备）         | 用于嵌入客户端的 AOAI API 版本                                                                | `str`   | `None`                   |
| `GRAPHRAG_EMBEDDING_API_ORGANIZATION`                   | AOAI（使用后备）         | 用于嵌入客户端的 AOAI 组织                                                                    | `str`   | `None`                   |
| `GRAPHRAG_EMBEDDING_API_PROXY`                          |                          | 用于嵌入客户端的 AOAI 代理                                                                    | `str`   | `None`                   |
| `GRAPHRAG_EMBEDDING_MODEL`                              |                          | 用于嵌入客户端的模型                                                                          | `str`   | `text-embedding-3-small` |
| `GRAPHRAG_EMBEDDING_BATCH_SIZE`                         |                          | 一次嵌入的文本数量。[（Azure 限制为 16）](https://learn.microsoft.com/en-us/azure/ai-ce)       | `int`   | 16                       |
| `GRAPHRAG_EMBEDDING_BATCH_MAX_TOKENS`                   |                          | 每批最大令牌数。[（Azure 限制为 8191）](https://learn.microsoft.com/en-us/azure/ai-services/openai/reference) | `int`   | 8191                     |
| `GRAPHRAG_EMBEDDING_TARGET`                             |                          | 要嵌入的目标字段。可以是 `required` 或 `all`                                                  | `str`   | `required`               |
| `GRAPHRAG_EMBEDDING_THREAD_COUNT`                       |                          | 用于嵌入并行化的线程数                                                                        | `int`   | 50                       |
| `GRAPHRAG_EMBEDDING_THREAD_STAGGER`                     |                          | 启动每个嵌入线程之间的等待时间（秒）                                                          | `float` | 0.3                      |
| `GRAPHRAG_EMBEDDING_CONCURRENT_REQUESTS`                |                          | 嵌入客户端允许的并发请求数                                                                    | `int`   | 25                       |
| `GRAPHRAG_EMBEDDING_TOKENS_PER_MINUTE`                  |                          | 嵌入客户端每分钟允许的令牌数。0 = 绕过                                                       | `int`   | 0                        |
| `GRAPHRAG_EMBEDDING_REQUESTS_PER_MINUTE`                |                          | 嵌入客户端每分钟允许的请求数。0 = 绕过                                                       | `int`   | 0                        |
| `GRAPHRAG_EMBEDDING_MAX_RETRIES`                        |                          | 请求失败时尝试的最大重试次数                                                                  | `int`   | 10                       |
| `GRAPHRAG_EMBEDDING_MAX_RETRY_WAIT`                     |                          | 重试之间等待的最大秒数                                                                        | `int`   | 10                       |
| `GRAPHRAG_EMBEDDING_SLEEP_ON_RATE_LIMIT_RECOMMENDATION` |                          | 是否在速率限制建议时休眠。（仅限 Azure）                                                      | `bool`  | `True`                   |

### 输入设置

这些设置控制管道使用的数据输入。任何具有后备的设置将使用基础 LLM 设置（如果可用）。

#### 纯文本输入数据 (`GRAPHRAG_INPUT_FILE_TYPE`=text)

| 参数                          | 描述                                                                                   | 类型  | 是否必需 | 默认值      |
| ----------------------------- | ------------------------------------------------------------------------------------- | ----- | -------- | ----------- |
| `GRAPHRAG_INPUT_FILE_PATTERN` | 从输入目录读取输入文件时使用的文件模式正则表达式                                       | `str` | 可选     | `.*\.txt$` |

#### CSV 输入数据 (`GRAPHRAG_INPUT_FILE_TYPE`=csv)

| 参数                                       | 描述                                                                                                                                                              | 类型  | 是否必需 | 默认值      |
| ------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- | -------- | ----------- |
| `GRAPHRAG_INPUT_TYPE`                       | 读取文件时使用的输入存储类型。（`file` 或 `blob`）                                                                                                                | `str` | 可选     | `file`      |
| `GRAPHRAG_INPUT_FILE_PATTERN`               | 从输入目录读取输入文件时使用的文件模式正则表达式                                                                                                                  | `str` | 可选     | `.*\.txt$`  |
| `GRAPHRAG_INPUT_TEXT_COLUMN`                | 读取 CSV 输入文件时使用的“text”列                                                                                                                                | `str` | 可选     | `text`      |
| `GRAPHRAG_INPUT_METADATA`                   | 以逗号分隔的 CSV 列列表，将其合并为 JSON 格式的元数据列                                                                                                          | `str` | 可选     | `None`      |
| `GRAPHRAG_INPUT_TITLE_COLUMN`               | 读取 CSV 输入文件时使用的“title”列                                                                                                                               | `str` | 可选     | `title`     |
| `GRAPHRAG_INPUT_STORAGE_ACCOUNT_BLOB_URL`   | 在 `blob` 模式下使用托管身份时使用的 Azure 存储 Blob 端点。格式为 `https://<storage_account_name>.blob.core.windows.net` | `str` | 可选     | `None`      |
| `GRAPHRAG_INPUT_CONNECTION_STRING`          | 从 Azure Blob 存储读取 CSV 输入文件时使用的连接字符串                                                                                                            | `str` | 可选     | `None`      |
| `GRAPHRAG_INPUT_CONTAINER_NAME`             | 从 Azure Blob 存储读取 CSV 输入文件时使用的容器名称                                                                                                              | `str` | 可选     | `None`      |
| `GRAPHRAG_INPUT_BASE_DIR`                   | 读取输入文件的基目录                                                                                                                                            | `str` | 可选     | `None`      |

### 数据映射设置

| 参数                          | 描述                                               | 类型  | 是否必需 | 默认值  |
| ----------------------------- | -------------------------------------------------- | ----- | -------- | ------- |
| `GRAPHRAG_INPUT_FILE_TYPE`    | 输入数据的类型，`csv` 或 `text`                    | `str` | 可选     | `text`  |
| `GRAPHRAG_INPUT_ENCODING`     | 读取 CSV/文本输入文件时应用的编码                   | `str` | 可选     | `utf-8` |

### 数据分块

| 参数                             | 描述                                                                                     | 类型  | 是否必需 | 默认值                       |
| ------------------------------- | --------------------------------------------------------------------------------------- | ----- | -------- | ----------------------------- |
| `GRAPHRAG_CHUNK_SIZE`           | 文本分块分析窗口的令牌数                                                                | `str` | 可选     | 1200                          |
| `GRAPHRAG_CHUNK_OVERLAP`        | 文本分块分析窗口的重叠令牌数                                                            | `str` | 可选     | 100                           |
| `GRAPHRAG_CHUNK_BY_COLUMNS`     | 在执行 TextUnit 分块时按文档属性分组的逗号分隔列表                                      | `str` | 可选     | `id`                          |
| `GRAPHRAG_CHUNK_ENCODING_MODEL` | 用于分块的编码模型                                                                      | `str` | 可选     | 顶级编码模型                  |

### 提示覆盖

| 参数                                           | 描述                                                                                      | 类型     | 是否必需 | 默认值                                                          |
| --------------------------------------------- | ---------------------------------------------------------------------------------------- | -------- | -------- | -------------------------------------------------------------- |
| `GRAPHRAG_ENTITY_EXTRACTION_PROMPT_FILE`      | 实体提取提示模板文本文件的路径（相对于根目录）                                            | `str`    | 可选     | `None`                                                         |
| `GRAPHRAG_ENTITY_EXTRACTION_MAX_GLEANINGS`    | 在循环中提取实体时调用的最大重试（收集）次数                                              | `int`    | 可选     | 1                                                              |
| `GRAPHRAG_ENTITY_EXTRACTION_ENTITY_TYPES`     | 要提取的实体类型的逗号分隔列表                                                            | `str`    | 可选     | `organization,person,event,geo`                                |
| `GRAPHRAG_ENTITY_EXTRACTION_ENCODING_MODEL`    | 用于实体提取的编码模型                                                                    | `str`    | 可选     | 顶级编码模型                                                    |
| `GRAPHRAG_SUMMARIZE_DESCRIPTIONS_PROMPT_FILE` | 描述摘要提示模板文本文件的路径（相对于根目录）                                            | `str`    | 可选     | `None`                                                         |
| `GRAPHRAG_SUMMARIZE_DESCRIPTIONS_MAX_LENGTH`   | 每个描述摘要生成的最大令牌数                                                              | `int`    | 可选     | 500                                                            |
| `GRAPHRAG_CLAIM_EXTRACTION_ENABLED`           | 是否为此管道启用声明提取                                                                  | `bool`   | 可选     | `False`                                                        |
| `GRAPHRAG_CLAIM_EXTRACTION_DESCRIPTION`       | 使用的声明描述提示参数                                                                    | `string` | 可选     | "Any claims or facts that could be relevant to threat analysis." |
| `GRAPHRAG_CLAIM_EXTRACTION_PROMPT_FILE`       | 使用的声明提取提示                                                                        | `string` | 可选     | `None`                                                         |
| `GRAPHRAG_CLAIM_EXTRACTION_MAX_GLEANINGS`     | 在循环中提取声明时调用的最大重试（收集）次数                                              | `int`    | 可选     | 1                                                              |
| `GRAPHRAG_CLAIM_EXTRACTION_ENCODING_MODEL`     | 用于声明提取的编码模型                                                                    | `str`    | 可选     | 顶级编码模型                                                    |
| `GRAPHRAG_COMMUNITY_REPORTS_PROMPT_FILE`      | 使用的社区报告提取提示                                                                    | `string` | 可选     | `None`                                                         |
| `GRAPHRAG_COMMUNITY_REPORTS_MAX_LENGTH`       | 每个社区报告生成的最大令牌数                                                              | `int`    | 可选     | 1500                                                           |

### 存储

本节控制管道用于导出输出表的存储机制。

| 参数                                        | 描述                                                                                                                                                              | 类型  | 是否必需 | 默认值 |
| ------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- | -------- | ------- |
| `GRAPHRAG_STORAGE_TYPE`                     | 使用的存储类型。选项为 `file`、`memory` 或 `blob`                                                                                                                | `str` | 可选     | `file`  |
| `GRAPHRAG_STORAGE_STORAGE_ACCOUNT_BLOB_URL` | 在 `blob` 模式下使用托管身份时使用的 Azure 存储 Blob 端点。格式为 `https://<storage_account_name>.blob.core.windows.net` | `str` | 可选     | None    |
| `GRAPHRAG_STORAGE_CONNECTION_STRING`        | 在 `blob` 模式下使用的 Azure 存储连接字符串                                                                                                                      | `str` | 可选     | None    |
| `GRAPHRAG_STORAGE_CONTAINER_NAME`           | 在 `blob` 模式下使用的 Azure 存储容器名称                                                                                                                        | `str` | 可选     | None    |
| `GRAPHRAG_STORAGE_BASE_DIR`                 | 数据输出的基路径                                                                                                                                                | `str` | 可选     | None    |

### 缓存

本节控制管道使用的缓存机制，用于缓存 LLM 调用结果。

| 参数                                       | 描述                                                                                                                                                              | 类型  | 是否必需 | 默认值 |
| ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- | -------- | ------- |
| `GRAPHRAG_CACHE_TYPE`                     | 使用的缓存类型。选项为 `file`、`memory`、`none` 或 `blob`                                                                                                        | `str` | 可选     | `file`  |
| `GRAPHRAG_CACHE_STORAGE_ACCOUNT_BLOB_URL` | 在 `blob` 模式下使用托管身份时使用的 Azure 存储 Blob 端点。格式为 `https://<storage_account_name>.blob.core.windows.net` | `str` | 可选     | None    |
| `GRAPHRAG_CACHE_CONNECTION_STRING`        | 在 `blob` 模式下使用的 Azure 存储连接字符串                                                                                                                      | `str` | 可选     | None    |
| `GRAPHRAG_CACHE_CONTAINER_NAME`           | 在 `blob` 模式下使用的 Azure 存储容器名称                                                                                                                        | `str` | 可选     | None    |
| `GRAPHRAG_CACHE_BASE_DIR`                 | 缓存文件的基路径                                                                                                                                                | `str` | 可选     | None    |

### 报告

本节控制管道用于常见事件和错误消息的报告机制。默认是将报告写入输出目录中的文件。您也可以选择将报告写入控制台或 Azure Blob 存储容器。

| 参数                                          | 描述                                                                                                                                                              | 类型  | 是否必需 | 默认值 |
| --------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- | -------- | ------- |
| `GRAPHRAG_REPORTING_TYPE`                     | 使用的报告器类型。选项为 `file`、`console` 或 `blob`                                                                                                             | `str` | 可选     | `file`  |
| `GRAPHRAG_REPORTING_STORAGE_ACCOUNT_BLOB_URL` | 在 `blob` 模式下使用托管身份时使用的 Azure 存储 Blob 端点。格式为 `https://<storage_account_name>.blob.core.windows.net` | `str` | 可选     | None    |
| `GRAPHRAG_REPORTING_CONNECTION_STRING`        | 在 `blob` 模式下使用的 Azure 存储连接字符串                                                                                                                      | `str` | 可选     | None    |
| `GRAPHRAG_REPORTING_CONTAINER_NAME`           | 在 `blob` 模式下使用的 Azure 存储容器名称                                                                                                                        | `str` | 可选     | None    |
| `GRAPHRAG_REPORTING_BASE_DIR`                 | 报告输出的基路径                                                                                                                                                | `str` | 可选     | None    |

### Node2Vec 参数

| 参数                           | 描述                                 | 类型   | 是否必需 | 默认值 |
| ----------------------------- | ------------------------------------ | ------ | -------- | ------- |
| `GRAPHRAG_NODE2VEC_ENABLED`    | 是否启用 Node2Vec                    | `bool` | 可选     | False   |
| `GRAPHRAG_NODE2VEC_NUM_WALKS`  | Node2Vec 执行的游走次数              | `int`  | 可选     | 10      |
| `GRAPHRAG_NODE2VEC_WALK_LENGTH`| Node2Vec 游走长度                    | `int`  | 可选     | 40      |
| `GRAPHRAG_NODE2VEC_WINDOW_SIZE`| Node2Vec 窗口大小                    | `int`  | 可选     | 2       |
| `GRAPHRAG_NODE2VEC_ITERATIONS` | 运行 Node2Vec 的迭代次数             | `int`  | 可选     | 3       |
| `GRAPHRAG_NODE2VEC_RANDOM_SEED`| Node2Vec 使用的随机种子              | `int`  | 可选     | 597832  |

### 数据快照

| 参数                                 | 描述                                   | 类型   | 是否必需 | 默认值 |
| ------------------------------------ | -------------------------------------- | ------ | -------- | ------- |
| `GRAPHRAG_SNAPSHOT_EMBEDDINGS`       | 是否启用嵌入快照                       | `bool` | 可选     | False   |
| `GRAPHRAG_SNAPSHOT_GRAPHML`          | 是否启用 GraphML 快照                  | `bool` | 可选     | False   |
| `GRAPHRAG_SNAPSHOT_RAW_ENTITIES`     | 是否启用原始实体快照                   | `bool` | 可选     | False   |
| `GRAPHRAG_SNAPSHOT_TOP_LEVEL_NODES`  | 是否启用顶级节点快照                   | `bool` | 可选     | False   |
| `GRAPHRAG_SNAPSHOT_TRANSIENT`        | 是否启用临时表快照                     | `bool` | 可选     | False   |

# 其他设置

| 参数                        | 描述                                                               | 类型   | 是否必需 | 默认值       |
| --------------------------- | ----------------------------------------------------------------- | ------ | -------- | ------------ |
| `GRAPHRAG_ASYNC_MODE`       | 使用的异步模式。可以是 `asyncio` 或 `threaded`                    | `str`  | 可选     | `asyncio`    |
| `GRAPHRAG_ENCODING_MODEL`   | 用于编码文本的文本编码模型，基于 tiktoken                         | `str`  | 可选     | `cl100k_base`|
| `GRAPHRAG_MAX_CLUSTER_SIZE` | 单个 Leiden 集群中包含的最大实体数                                | `int`  | 可选     | 10           |
| `GRAPHRAG_UMAP_ENABLED`     | 是否启用 UMAP 布局                                                | `bool` | 可选     | False        |