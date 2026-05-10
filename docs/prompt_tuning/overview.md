# 提示调整 ⚙️

本页面概述了 GraphRAG 索引引擎可用的提示调整选项。

## 默认提示

默认提示是开始使用 GraphRAG 系统的最简单方式。它设计为开箱即用，需最少的配置。有关索引和查询的默认提示的更多细节，请参阅[手动调整](./manual_prompt_tuning.md)页面。

## 自动调整

Auto Tuning leverages your input data and LLM interactions to create domain-adapted prompts for the generation of the knowledge graph. It is highly encouraged to run it as it will yield better results when executing an Index Run. For more details about how to use it, please refer to the [Auto Tuning](auto_prompt_tuning.md) page.

## 手动调整

Manual tuning is an advanced use-case. Most users will want to use the Auto Tuning feature instead. Details about how to use manual configuration are available in the [manual tuning](manual_prompt_tuning.md) page.
