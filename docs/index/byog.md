# 自带图表

一些用户询问是否可以自带现有图表，并将其汇总后用于 GraphRAG 查询。有很多方法可以实现这一点，但这里我们将介绍一种与现有 GraphRAG 工作流程轻松兼容的简单方法。

为了涵盖 GraphRAG 查询的基本用例，您应该从数据中派生出两到三个表：

- entities.parquet - 这是在数据集中找到的实体列表，这些实体是图表的节点。
- relationships.parquet - 这是在数据集中找到的关系列表，这些关系是图表的边。
- text_units.parquet - 这是提取图表的源文本块。这是可选的，具体取决于您打算使用的查询方法（稍后介绍）。

这里描述的方法是运行一个自定义的 GraphRAG 工作流程流水线，该流程假定文本分块、实体提取和关系提取已经完成。

## 表格

### 实体

查看完整实体[表结构](./outputs.md#entities)。为了进行图形汇总，您只需要 id、title、description 和 text_unit_id 列表。

其他属性用于可选的图形可视化。

### 关系

查看完整关系[表结构](./outputs.md#relationships)。为了进行图形汇总，您只需要 id、source、target、description、weight 和 text_unit_id 列表。

> 注意：`weight` 字段非常重要，因为它用于正确计算莱顿社区！

## 工作流配置

GraphRAG 可以指定*仅*您需要的特定工作流步骤。对于基本的图汇总和查询，您需要在 settings.yaml 中添加以下配置：

```yaml
workflows: [create_communities, create_community_reports]
```

这将仅生成 GraphRAG [全局搜索](../query/global_search.md) 所需的最少工作流。

## 可选附加配置

如果您想运行 [本地搜索](../query/local_search.md)、[DRIFT搜索](../query/drift_search.md) 或 [基本搜索](../query/overview.md#basic-search)，则需要添加 text_units 和一些嵌入。

### 文本单元

查看完整的 text_units [表架构](./outputs.md#text_units)。文本单元是文档的块，其大小经过调整以确保其适合模型的上下文窗口。某些搜索方法会使用文本单元，因此如果您有文本单元，则可能需要将其添加到文档中。

### 扩展配置

要执行上述其他搜索类型，您需要嵌入部分内容。只需添加嵌入工作流：

```yaml
workflows: [create_communities, create_community_reports, generate_text_embeddings]
```

### FastGraphRAG

[FastGraphRAG](./methods.md#fastgraphrag) 使用文本单元 (text_units) 来表示社区报告，而不是实体和关系描述。如果您的图的来源方式使其没有描述，这可能是一个有用的替代方案。在这种情况下，您需要更新工作流列表以包含文本变体：

```yaml
workflows: [create_communities, create_community_reports_text, generate_text_embeddings]
```

此方法要求您的实体和关系表具有指向 text_unit_id 列表的有效链接。另请注意，只有在执行除全局搜索之外的搜索时，才需要 `generate_text_embeddings`。

## 设置

整合：

- `input`：即使您不需要我们处理，GraphRAG 也需要一个输入文档集。您可以创建一个输入文件夹，并将一个 dummy.txt 文档放入其中以解决这个问题。
- `output`：创建一个输出文件夹，并将您的实体和关系（以及可选的 text_units）Parquet 文件放入其中。
- 如上所述更新您的配置，以便仅运行您需要的工作流子集。
- 运行`graphrag index --root <你的项目根目录>`
