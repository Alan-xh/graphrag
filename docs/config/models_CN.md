# 语言模型选择与覆盖

本页包含有关选择使用模型以及为 GraphRAG 提供自定义模型选项的信息。请注意，这不是指导您为特定用例选择合适模型的指南。

## 默认模型支持

GraphRAG 使用 OpenAI 模型进行构建和测试，因此这是我们默认支持的模型集。这并非意在限制或声明其质量或适合您的用例，而仅表示这是我们在提示、调优和调试方面最熟悉的模型集。

GraphRAG 还利用了我们团队内多个项目使用的语言模型包装库，称为 fnllm。fnllm 为 GraphRAG 提供了两个重要功能：速率限制配置，以帮助我们在大型索引任务中最大化吞吐量；以及 API 调用的健壮缓存，以在测试、实验或增量摄取的重复索引中最小化消耗。fnllm 在底层使用 OpenAI Python SDK，因此 OpenAI 兼容的端点是开箱即用的基本要求。

## 模型选择注意事项

GraphRAG 已使用 OpenAI 的 gpt-4 系列模型（包括 gpt-4、gpt-4-turbo、gpt-4o 和 gpt-4o-mini）进行了最彻底的测试。例如，我们的 [arXiv 论文](https://arxiv.org/abs/2404.16130) 使用 gpt-4-turbo 进行了质量评估。

在 2.2.0 版本之前的 GraphRAG 广泛使用了 `max_tokens` 和 `logit_bias` 来控制生成响应的长度或内容。引入 o 系列模型后，添加了不兼容的新参数，因为这些模型包含的推理组件与非推理模型相比具有不同的消耗模式和响应生成属性。GraphRAG 2.2.0 现已支持这些模型，但在切换之前需要了解一些重要差异。

- 之前，GraphRAG 在某些地方使用 `max_tokens` 来限制响应长度，以确保在构建下游上下文窗口进行摘要时具有可预测的内容大小。我们现在已从使用 `max_tokens` 切换到使用提示方法，这在我们的测试中效果良好。我们建议仅出于预算原因在语言模型配置中使用 `max_tokens` 来限制消耗，而不用于控制预期响应长度。我们现在还支持 o 系列等效的 `max_completion_tokens`，但如果使用此参数，请注意，除了响应令牌外，可能还有一些未知的固定推理消耗量，因此它不是控制响应的好方法。
- 之前，GraphRAG 使用 `max_tokens` 和 `logit_bias` 的组合来严格控制提取过程中的二元是/否问题。由于推理模型无法做到这一点，我们再次切换到提示方法。我们对 gpt-4o、gpt-4o-mini 和 o1 的测试表明，这是一致的，但如果您使用较旧或较小的模型，可能会出现问题。
- o 系列模型的速度慢得多且成本更高。在配置中采用非对称模型使用方法可能是有用的：您可以在 settings.yaml 的 `models` 块中定义任意数量的模型，并通过键为每个需要语言模型的工作流引用它们。例如，您可以为索引使用 gpt-4o，为查询使用 o1。进行实验以找到适合您用例的成本、速度和质量的正确平衡。
- o 系列模型包含一种原生的链式推理形式，这在非 o 系列模型中不存在。GraphRAG 的提示有时包含 CoT，因为这在 gpt-4* 系列中是一种有效技术。但在 o 系列中可能会适得其反，因此您可能需要调整甚至重写大部分提示模板（特别是图和声明提取部分）。

非对称模型使用的示例配置：

```yaml
models:
  extraction_chat_model:
    api_key: ${GRAPHRAG_API_KEY}
    type: openai_chat
    auth_type: api_key
    model: gpt-4o
    model_supports_json: true
  query_chat_model:
    api_key: ${GRAPHRAG_API_KEY}
    type: openai_chat
    auth_type: api_key
    model: o1
    model_supports_json: true

...

extract_graph:
  model_id: extraction_chat_model
  P: "prompts/extract_graph.txt"
  entity_types: [organization,person,geo,event]
  max_gleanings: 1

...

global_search:
  chat_model_id: query_chat_model
  map_prompt: "prompts/global_search_map_system_prompt.txt"
  reduce_prompt: "prompts/global_search_reduce_system_prompt.txt"
  knowledge_prompt: "prompts/global_search_knowledge_system_prompt.txt"
```

另一个选择是完全不使用语言模型进行图提取，而是使用 `fast` [索引方法](../index/methods.md)，该方法在索引阶段的某些部分使用 NLP 替代 LLM API。

## 使用非 OpenAI 模型

如上所述，我们的主要经验和重点集中在 OpenAI 模型上，因此这是开箱即用的支持内容。许多用户请求支持其他模型类型，但处理当今可用的众多模型超出了我们的研究范围。您可以使用以下两种方法连接到非 OpenAI 模型：

### 代理 API

许多用户使用 [ollama](https://ollama.com/) 等平台将底层的模型 HTTP 调用代理到不同的模型提供商。这似乎效果不错，但我们经常看到响应格式错误（尤其是 JSON）的问题，因此如果您这样做，请确保您的模型能够可靠地返回 GraphRAG 期望的特定响应格式。如果模型出现问题，您可能需要尝试调整提示以引导格式，或者在代理中拦截响应以处理格式错误的响应。

### 模型协议

从 GraphRAG 2.0.0 开始，我们通过使用标准的聊天和嵌入协议以及附带的 ModelFactory 支持模型注入，您可以使用它来注册您的模型实现。这不支持 CLI，因此您需要将 GraphRAG 用作库。

- 我们的协议 [定义在此处](https://github.com/microsoft/graphrag/blob/main/graphrag/language_model/protocol/base.py)
- 我们的基础实现，包装了 fnllm，[在此处](https://github.com/microsoft/graphrag/blob/main/graphrag/language_model/providers/fnllm/models.py)
- 我们在测试中有一个简单的模拟实现，您可以 [参考此处](https://github.com/microsoft/graphrag/blob/main/tests/mock_provider.py)

一旦您有了模型实现，您需要使用 ModelFactory 注册它：

```python
class MyCustomModel:
    ...
    # 实现

# 在其他地方...
ModelFactory.register_chat("my-custom-chat-model", lambda **kwargs: MyCustomModel(**kwargs))
```

然后在您的配置中，您可以引用您使用的类型名称：

```yaml
models:
  default_chat_model:
    type: my-custom-chat-model

extract_graph:
  model_id: default_chat_model
  prompt: "prompts/extract_graph.txt"
  entity_types: [organization,person,geo,event]
  max_gleanings: 1
```

请注意，您的自定义模型将接收 GraphRAG 中使用的相同初始化和方法调用参数。目前无法定义自定义参数，因此您可能需要在实现中使用闭包作用域或工厂模式来获取自定义配置值。


# LanguageModelConfig 参数
- api_key (str | None):

描述：用于 LLM 服务的 API 密钥。
默认值：language_model_defaults.api_key
验证：
当 auth_type 为 AuthType.APIKey 时，API 密钥是必需的。
当 auth_type 为 AuthType.AzureManagedIdentity 时，不得提供 API 密钥。
如果 API 密钥缺失且为必需，则抛出 ApiKeyMissingError 异常。
如果 API 密钥在不应提供的情况下（例如，与 Azure 托管身份一起使用时）提供，则抛出 ConflictingSettingsError 异常。
- auth_type (AuthType):

描述：用于 LLM 服务的认证类型。
默认值：language_model_defaults.auth_type
验证：
如果 auth_type 为 AuthType.AzureManagedIdentity，则 type 不能是 ModelType.OpenAIChat 或 ModelType.OpenAIEmbedding。
如果认证类型与正在使用的模型类型冲突，则抛出 ConflictingSettingsError 异常。
- type (ModelType | str):

描述：要使用的 LLM 模型类型（例如，聊天模型、嵌入模型）。
验证：
必须是 ModelFactory 支持的已识别模型类型。
如果模型类型无法识别，则抛出 KeyError 异常。
- model (str):

描述：要使用的特定 LLM 模型名称（例如，“gpt-4”、“text-embedding-ada-002”）。
- encoding_model (str):

描述：要使用的编码模型，主要用于分词。
默认值：language_model_defaults.encoding_model
验证：
如果为空字符串，它将尝试使用 tiktoken.encoding_name_for_model() 从 model 字段推断编码模型。
如果推断或提供的编码模型名称无法识别，则抛出 KeyError 异常。
- api_base (str | None):

描述：LLM API 端点的基础 URL。
默认值：language_model_defaults.api_base


### 高级配置字段

* **`organization`** (str | None):
    * **描述**：用于 LLM 服务的组织。
    * **默认值**：`language_model_defaults.organization`

* **`proxy`** (str | None):
    * **描述**：用于 LLM 服务的代理地址。
    * **默认值**：`language_model_defaults.proxy`

* **`audience`** (str | None):
    * **描述**：当使用托管身份进行 LLM 连接时，Azure 资源的 URI。
    * **默认值**：`language_model_defaults.audience`

* **`model_supports_json`** (bool | None):
    * **描述**：指示模型是否支持 JSON 输出模式。
    * **默认值**：`language_model_defaults.model_supports_json`

* **`request_timeout`** (float):
    * **描述**：LLM 请求的超时时间（秒）。
    * **默认值**：`language_model_defaults.request_timeout`

* **`tokens_per_minute`** (int | Literal["auto"] | None):
    * **描述**：LLM 服务每分钟允许处理的令牌数量。可以设置为具体数值或 `"auto"`。
    * **默认值**：`language_model_defaults.tokens_per_minute`

* **`requests_per_minute`** (int | Literal["auto"] | None):
    * **描述**：LLM 服务每分钟允许发起的请求数量。可以设置为具体数值或 `"auto"`。
    * **默认值**：`language_model_defaults.requests_per_minute`

* **`retry_strategy`** (str):
    * **描述**：LLM 服务的重试策略。
    * **默认值**：`language_model_defaults.retry_strategy`

* **`max_retries`** (int):
    * **描述**：LLM 服务允许的最大重试次数。
    * **默认值**：`language_model_defaults.max_retries`

* **`max_retry_wait`** (float):
    * **描述**：LLM 服务重试之间的最大等待时间（秒）。
    * **默认值**：`language_model_defaults.max_retry_wait`

* **`concurrent_requests`** (int):
    * **描述**：LLM 服务是否使用并发请求，以及允许的最大并发请求数。
    * **默认值**：`language_model_defaults.concurrent_requests`

* **`async_mode`** (AsyncType):
    * **描述**：要使用的异步模式。
    * **默认值**：`language_model_defaults.async_mode`

* **`responses`** (list[str | BaseModel] | None):
    * **描述**：在模拟模式下使用的静态响应列表。
    * **默认值**：`language_model_defaults.responses`

* **`max_tokens`** (int | None):
    * **描述**：要生成的最大令牌数量。
    * **默认值**：`language_model_defaults.max_tokens`

* **`temperature`** (float):
    * **描述**：用于令牌生成的温度值，影响输出的随机性。值越高，输出越随机。
    * **默认值**：`language_model_defaults.temperature`

* **`max_completion_tokens`** (int | None):
    * **描述**：要消耗的最大令牌数量。这包括 O* 推理模型的推理令牌。
    * **默认值**：`language_model_defaults.max_completion_tokens`

* **`reasoning_effort`** (str | None):
    * **描述**：OpenAI 推理模型应花费的努力级别。支持的选项有 `'low'`、`'medium'`、`'high'`；OAI 默认为 `'medium'`。
    * **默认值**：`language_model_defaults.reasoning_effort`

* **`top_p`** (float):
    * **描述**：用于令牌生成的 top-p 值。
    * **默认值**：`language_model_defaults.top_p`

* **`n`** (int):
    * **描述**：要生成的完成数量。
    * **默认值**：`language_model_defaults.n`

* **`frequency_penalty`** (float):
    * **描述**：用于令牌生成的频率惩罚。值越高，模型越不容易重复出现过的词语。
    * **默认值**：`language_model_defaults.frequency_penalty`

* **`presence_penalty`** (float):
    * **描述**：用于令牌存在的惩罚。值越高，模型越不容易生成训练数据中已经出现过的词语。
    * **默认值**：`language_model_defaults.presence_penalty`

---