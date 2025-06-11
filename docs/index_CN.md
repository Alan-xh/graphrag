# 欢迎体验 GraphRAG

👉 [微软研究博客文章](https://www.microsoft.com/en-us/research/blog/graphrag-unlocking-llm-discovery-on-narrative-private-data/) <br/>
👉 [GraphRAG 加速器](https://github.com/Azure-Samples/graphrag-accelerator) <br/>
👉 [GraphRAG Arxiv](https://arxiv.org/pdf/2404.16130)

<p align="center">
<img src="img/GraphRag-Figure1.jpg" alt="图1：使用 GPT-4 Turbo 从私有数据集构建的 LLM 生成的知识图谱。" width="450" align="center" />
</p>
<p align="center">
图1：使用 GPT-4 Turbo 构建的 LLM 生成的知识图谱。
</p>

GraphRAG 是一种结构化、层次化的检索增强生成（Retrieval Augmented Generation，简称 RAG）方法，相较于使用纯文本片段的朴素语义搜索方法。GraphRAG 过程包括从原始文本中提取知识图谱，构建社区层次结构，为这些社区生成摘要，然后在执行基于 RAG 的任务时利用这些结构。

要了解更多关于 GraphRAG 及其如何增强语言模型对私有数据的推理能力，请访问 [微软研究博客文章](https://www.microsoft.com/en-us/research/blog/graphrag-unlocking-llm-discovery-on-narrative-private-data/)。

## 解决方案加速器 🚀

要快速启动 GraphRAG 系统，我们推荐尝试 [解决方案加速器](https://github.com/Azure-Samples/graphrag-accelerator) 包。此包提供了一个用户友好的端到端体验，结合了 Azure 资源。

## 开始使用 GraphRAG 🚀

要开始使用 GraphRAG，请查看 [_快速入门_](get_started.md) 指南。
如需深入了解主要子系统，请访问 [索引器](index/overview.md) 和 [查询](query/overview.md) 包的文档页面。

## GraphRAG 与基准 RAG 对比 🔍

检索增强生成（RAG）是一种利用现实世界信息改善 LLM 输出的技术。这项技术是大多数基于 LLM 的工具的重要组成部分，大多数 RAG 方法使用向量相似性作为搜索技术，我们称之为 _基准 RAG_。GraphRAG 使用知识图谱在处理复杂信息的问答性能上提供了显著改进。RAG 技术在帮助 LLM 推理 _私有数据集_（即 LLM 未训练且从未见过的数据，例如企业的专有研究、商业文档或通信）方面显示出潜力。_基准 RAG_ 旨在解决这一问题，但我们观察到在某些情况下基准 RAG 表现得很差。例如：

- 基准 RAG 难以“连接点”。当回答问题需要通过共享属性遍历分散的信息片段以提供新的综合见解时，会出现这种情况。
- 基准 RAG 在被要求整体理解大型数据集合或单个大型文档的总结语义概念时表现不佳。

为了解决这一问题，技术社区正在开发扩展和增强 RAG 的方法。微软研究的 GraphRAG 新方法基于输入语料库创建知识图谱。这一图谱，连同社区摘要和图机器学习输出，在查询时用于增强提示。GraphRAG 在回答上述两类问题时表现出显著的改进，展现出在私有数据集上超越其他方法的智能或精通表现。

## GraphRAG 流程 🤖

GraphRAG 建立在我们先前的 [研究](https://www.microsoft.com/en-us/worklab/patterns-hidden-inside-the-org-chart) 和 [工具](https://github.com/graspologic-org/graspologic) 的基础上，使用图机器学习。GraphRAG 流程的基本步骤如下：

### 索引

- 将输入语料库切分为一系列文本单元（TextUnits），这些单元作为后续过程的可分析单位，并为我们的输出提供细粒度引用。
- 从文本单元中提取所有实体、关系和关键声明。
- 使用 [Leiden 技术](https://arxiv.org/pdf/1810.08473.pdf) 对图进行层次聚类。如需直观了解，请查看上方的图1。每个圆圈代表一个实体（例如人、地点或组织），大小表示实体的度，颜色表示其社区。
- 从底部向上为每个社区及其组成部分生成摘要。这有助于整体理解数据集。

### 查询

在查询时，这些结构用于为 LLM 上下文窗口提供材料以回答问题。主要查询模式包括：

- [_全局搜索_](query/global_search.md)：通过利用社区摘要来推理关于语料库的整体问题。
- [_局部搜索_](query/local_search.md)：通过扩展到特定实体的邻居和相关概念来推理特定实体。
- [_DRIFT 搜索_](query/drift_search.md)：通过扩展到特定实体的邻居和相关概念来推理特定实体，但增加了社区信息的上下文。

### 提示调优

直接使用 GraphRAG 处理您的数据可能无法获得最佳结果。
我们强烈建议按照我们文档中的 [提示调优指南](prompt_tuning/overview.md) 进行提示微调。

## 版本管理

请查看 [重大变更](https://github.com/microsoft/graphrag/blob/main/breaking-changes.md) 文档，了解我们对项目版本管理的方法。

*在次要版本更新之间，始终运行 `graphrag init --root [path] --force` 以确保使用最新的配置格式。在主要版本更新之间运行提供的迁移笔记本，以避免重新索引先前的数据集。请注意，这将覆盖您的配置和提示，因此如有需要请备份。*