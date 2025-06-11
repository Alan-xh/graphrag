# 入门指南

## 要求

[Python 3.10-3.12](https://www.python.org/downloads/)

要开始使用 GraphRAG 系统，您有以下几种选择：

👉 [使用 GraphRAG 加速器解决方案](https://github.com/Azure-Samples/graphrag-accelerator) <br/>
👉 [从 PyPI 安装](https://pypi.org/project/graphrag/) <br/>
👉 [从源码使用](developing.md)<br/>

以下是一个使用 GraphRAG 系统的简单端到端示例，采用从 PyPI 安装的选项。

它展示了如何使用系统对一些文本进行索引，然后使用索引数据回答关于文档的问题。

# 安装 GraphRAG

```bash
pip install graphrag
```

# 运行索引器

我们需要设置一个数据项目和一些初始配置。首先，准备一个样本数据集：

```sh
mkdir -p ./ragtest/input
```

从可信来源获取查尔斯·狄更斯的《圣诞颂歌》副本：

```sh
curl https://www.gutenberg.org/cache/epub/24022/pg24022.txt -o ./ragtest/input/book.txt
```

## 设置工作空间变量

要初始化您的工作空间，首先运行 `graphrag init` 命令。
由于我们在上一步已经配置了一个名为 `./ragtest` 的目录，运行以下命令：

```sh
graphrag init --root ./ragtest
```

这将在 `./ragtest` 目录中创建两个文件：`.env` 和 `settings.yaml`。

- `.env` 包含运行 GraphRAG 管道所需的环境变量。如果您检查该文件，将看到定义的单个环境变量：
  `GRAPHRAG_API_KEY=<API_KEY>`。将 `<API_KEY>` 替换为您自己的 OpenAI 或 Azure API 密钥。
- `settings.yaml` 包含管道的设置。您可以修改此文件以更改管道的设置。
  <br/>

### 使用 OpenAI

如果以 OpenAI 模式运行，您只需更新 `.env` 文件中 `GRAPHRAG_API_KEY` 的值，填入您的 OpenAI API 密钥。

### 使用 Azure OpenAI

除了设置您的 API 密钥外，Azure OpenAI 用户还应在 `settings.yaml` 文件中设置以下变量。要找到相应的部分，只需搜索 `models:` 根配置；您应该会看到两个部分，一个用于默认聊天端点，一个用于默认嵌入端点。以下是添加到聊天模型配置的示例：

```yaml
type: azure_openai_chat # 对于嵌入端点使用 azure_openai_embedding
api_base: https://<instance>.openai.azure.com
api_version: 2024-02-15-preview # 您可以根据需要自定义其他版本
deployment_name: <azure_model_deployment_name>
```

#### 在 Azure 上使用托管身份验证
要使用托管身份验证，请在模型配置中添加一个额外值，并注释掉或删除 `api_key` 行：

```yaml
auth_type: azure_managed_identity # 默认 auth_type 为 api_key
# api_key: ${GRAPHRAG_API_KEY}
```

您还需要使用 [az login](https://learn.microsoft.com/en-us/cli/azure/authenticate-azure-cli) 登录并选择包含您的端点的订阅。

## 运行索引管道

最后，我们将运行管道！

```sh
graphrag index --root ./ragtest
```

![从 CLI 执行的管道](img/pipeline-running.png)

此过程将需要一些时间运行。具体时间取决于您的输入数据大小、使用的模型以及使用的文本块大小（这些可以在您的 `settings.yaml` 文件中配置）。
管道完成后，您应该会看到一个名为 `./ragtest/output` 的新文件夹，其中包含一系列 parquet 文件。

# 使用查询引擎

现在让我们使用这个数据集提出一些问题。

以下是使用全局搜索提出高层次问题的示例：

```sh
graphrag query \
--root ./ragtest \
--method global \
--query "这个故事的主要主题是什么？"
```

以下是使用局部搜索询问关于特定角色的更具体问题的示例：

```sh
graphrag query \
--root ./ragtest \
--method local \
--query "斯克罗吉是谁？他的主要关系是什么？"
```

请参阅 [查询引擎](query/overview.md) 文档，以获取有关如何在索引器完成执行后，利用我们的局部和全局搜索机制从数据中提取有意义见解的详细信息。

# 深入了解

- 有关配置 GraphRAG 的更多详情，请参见 [配置文档](config/overview.md)。
- 要了解更多关于初始化的信息，请参阅 [初始化文档](config/init.md)。
- 有关使用 CLI 的更多详情，请参阅 [CLI 文档](cli.md)。
- 查看我们的 [可视化指南](visualization_guide.md)，以获得更交互式的知识图调试和探索体验。