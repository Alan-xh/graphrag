# GraphRAG

👉 [使用 GraphRAG 加速器解决方案](https://github.com/Azure-Samples/graphrag-accelerator) <br/>
👉 [微软研究博客文章](https://www.microsoft.com/en-us/research/blog/graphrag-unlocking-llm-discovery-on-narrative-private-data/)<br/>
👉 [阅读文档](https://microsoft.github.io/graphrag)<br/>
👉 [GraphRAG Arxiv](https://arxiv.org/pdf/2404.16130)

<div align="left">
  <a href="https://pypi.org/project/graphrag/">
    <img alt="PyPI - 版本" src="https://img.shields.io/pypi/v/graphrag">
  </a>
  <a href="https://pypi.org/project/graphrag/">
    <img alt="PyPI - 下载量" src="https://img.shields.io/pypi/dm/graphrag">
  </a>
  <a href="https://github.com/microsoft/graphrag/issues">
    <img alt="GitHub 问题" src="https://img.shields.io/github/issues/microsoft/graphrag">
  </a>
  <a href="https://github.com/microsoft/graphrag/discussions">
    <img alt="GitHub 讨论" src="https://img.shields.io/github/discussions/microsoft/graphrag">
  </a>
</div>

## 概述

GraphRAG 项目是一个数据管道和转换套件，旨在利用大语言模型（LLMs）的能力从非结构化文本中提取有意义的结构化数据。

要了解更多关于 GraphRAG 及其如何增强您的 LLM 对私有数据推理能力的信息，请访问 <a href="https://www.microsoft.com/en-us/research/blog/graphrag-unlocking-llm-discovery-on-narrative-private-data/" target="_blank">微软研究博客文章</a>。

## 快速入门

要开始使用 GraphRAG 系统，我们建议尝试 [解决方案加速器](https://github.com/Azure-Samples/graphrag-accelerator) 包。此包提供了一个用户友好的端到端体验，结合了 Azure 资源。

## 仓库指南

本仓库介绍了一种使用知识图谱记忆结构来增强 LLM 输出的方法。请注意，提供的代码仅作为演示，并非微软官方支持的产品。

⚠️ *警告：GraphRAG 索引操作可能成本较高，请阅读所有文档以了解流程和相关费用，并从小规模开始。*

## 深入了解

- 要了解我们的贡献指南，请参见 [CONTRIBUTING.md](./CONTRIBUTING.md)
- 要开始开发 _GraphRAG_，请参见 [DEVELOPING.md](./DEVELOPING.md)
- 加入讨论并在 [GitHub 讨论区](https://github.com/microsoft/graphrag/discussions) 提供反馈！

## 提示调优

直接使用 _GraphRAG_ 处理您的数据可能无法获得最佳结果。
我们强烈建议根据我们的文档中的 [提示调优指南](https://microsoft.github.io/graphrag/prompt_tuning/overview/) 进行提示微调。

## 版本控制

请参阅 [重大变更](./breaking-changes.md) 文档，了解我们对项目版本控制的方法。

*在次要版本更新之间，始终运行 `graphrag init --root [path] --force` 以确保您拥有最新的配置格式。在主要版本更新之间运行提供的迁移笔记本，以避免重新索引先前的数据集。请注意，这将覆盖您的配置和提示，因此请根据需要进行备份。*

## 负责任 AI 常见问题解答

参见 [RAI_TRANSPARENCY.md](./RAI_TRANSPARENCY.md)

- [什么是 GraphRAG？](./RAI_TRANSPARENCY.md#what-is-graphrag)
- [GraphRAG 能做什么？](./RAI_TRANSPARENCY.md#what-can-graphrag-do)
- [GraphRAG 的预期用途是什么？](./RAI_TRANSPARENCY.md#what-are-graphrags-intended-uses)
- [GraphRAG 如何评估？使用哪些指标来衡量性能？](./RAI_TRANSPARENCY.md#how-was-graphrag-evaluated-what-metrics-are-used-to-measure-performance)
- [GraphRAG 的局限性是什么？用户如何在使用系统时最大程度减少 GraphRAG 局限性的影响？](./RAI_TRANSPARENCY.md#what-are-the-limitations-of-graphrag-how-can-users-minimize-the-impact-of-graphrags-limitations-when-using-the-system)
- [哪些操作因素和设置能够实现 GraphRAG 的有效和负责任使用？](./RAI_TRANSPARENCY.md#what-operational-factors-and-settings-allow-for-effective-and-responsible-use-of-graphrag)

## 商标

本项目可能包含项目、产品或服务的商标或标志。使用微软商标或标志需遵守
[微软的商标与品牌指南](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general)。
在本项目的修改版本中使用微软商标或标志不得引起混淆或暗示微软的赞助。
任何第三方商标或标志的使用均须遵守相关第三方的政策。

## 隐私

[微软隐私声明](https://privacy.microsoft.com/en-us/privacystatement)