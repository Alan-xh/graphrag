# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

"""Encapsulates pipeline construction and selection."""

from typing import ClassVar

from graphrag.config.enums import IndexingMethod
from graphrag.config.models.graph_rag_config import GraphRagConfig
from graphrag.index.typing.pipeline import Pipeline
from graphrag.index.typing.workflow import WorkflowFunction


class PipelineFactory:
    """A factory class for workflow pipelines."""

    workflows: ClassVar[dict[str, WorkflowFunction]] = {}

    @classmethod
    def register(cls, name: str, workflow: WorkflowFunction):
        """Register a custom workflow function."""
        cls.workflows[name] = workflow

    @classmethod
    def register_all(cls, workflows: dict[str, WorkflowFunction]):
        """Register a dict of custom workflow functions."""
        for name, workflow in workflows.items():
            cls.register(name, workflow)

    @classmethod
    def create_pipeline(
        cls,
        config: GraphRagConfig,
        method: IndexingMethod = IndexingMethod.Standard,
        is_update_run: bool = False,
    ) -> Pipeline:
        """Create a pipeline generator."""
<<<<<<< HEAD
        workflows = _get_workflows_list(config, method, is_update_run)
        return Pipeline([(name, cls.workflows[name]) for name in workflows])
=======
        workflows = _get_workflows_list(config, method, is_update_run) # 获得 workflow 列表
        return Pipeline([(name, cls.workflows[name]) for name in workflows]) # [{name, class}]
>>>>>>> origin


def _get_workflows_list(
    config: GraphRagConfig,
    method: IndexingMethod = IndexingMethod.Standard,
    is_update_run: bool = False,
) -> list[str]:
    """Return a list of workflows for the indexing pipeline."""
    update_workflows = [
        "update_final_documents",
        "update_entities_relationships",
        "update_text_units",
        "update_covariates",
        "update_communities",
        "update_community_reports",
        "update_text_embeddings",
        "update_clean_state",
    ]
    if config.workflows:
        return config.workflows

    match method:
        case IndexingMethod.Standard:
            return [
<<<<<<< HEAD
                "create_base_text_units",
                "create_final_documents",
                "extract_graph",
                "finalize_graph",
                *(["extract_covariates"] if config.extract_claims.enabled else []),
                "create_communities",
                "create_final_text_units",
                "create_community_reports",
                "generate_text_embeddings",
=======
                "create_base_text_units", # 构建文档单元
                "create_final_documents", # 构建文档
                "extract_graph", # prompt 构建图谱
                "finalize_graph", # 完成图表
                *(["extract_covariates"] if config.extract_claims.enabled else []),
                "create_communities", # 创建社区
                "create_final_text_units", # 创建最终的文本单元
                "create_community_reports", # 创建社区报告
                "generate_text_embeddings", # 生成文本嵌入
>>>>>>> origin
                *(update_workflows if is_update_run else []),
            ]
        case IndexingMethod.Fast:
            return [
                "create_base_text_units",
                "create_final_documents",
<<<<<<< HEAD
                "extract_graph_nlp",
                "prune_graph",
=======
                "extract_graph_nlp", # nlp 构建图谱
                "prune_graph", # 剪枝
>>>>>>> origin
                "finalize_graph",
                "create_communities",
                "create_final_text_units",
                "create_community_reports_text",
                "generate_text_embeddings",
                *(update_workflows if is_update_run else []),
            ]
