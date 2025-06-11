# GraphRAG 开发

# 要求

| 名称                | 安装方法                                                     | 用途                                                                               |
| ------------------- | ------------------------------------------------------------ | --------------------------------------------------------------------------------- |
| Python 3.10 或 3.11 | [下载](https://www.python.org/downloads/)                    | 该库基于 Python 开发。                                                            |
| Poetry              | [说明](https://python-poetry.org/docs/#installation)         | Poetry 用于 Python 代码库的包管理和虚拟环境管理。                                  |

# 入门指南

## 安装依赖
```shell
# 安装 Python 依赖
poetry install
```

## 执行索引引擎
```shell
poetry run poe index <...args>
```

## 执行提示调优
```shell
poetry run poe prompt_tune <...args>
```

## 执行查询
```shell
poetry run poe query <...args>
```

## 仓库结构
以下是仓库顶层文件夹结构的概述，详细说明了整体设计和用途。
我们尽可能采用工厂设计模式，使得 graphrag 的每个核心组件可以支持多种实现方式。

```shell
graphrag
├── api             # 库的 API 定义
├── cache           # 缓存模块，支持多种选项
│   └─ factory.py   #  └─ 创建缓存的主要入口
├── callbacks       # 常用的回调函数集合
├── cli             # 库的命令行界面
│   └─ main.py      #  └─ 主命令行入口
├── config          # 配置管理
├── index           # 索引引擎
|    └─ run/run.py  #  构建索引的主要入口
├── logger          # 日志模块，支持多种选项
│   └─ factory.py   #  └─ 创建日志的主要入口
├── model           # 与知识图谱相关的数据模型定义
├── prompt_tune     # 提示调优模块
├── prompts         # graphrag 使用的所有系统提示集合
├── query           # 查询引擎
├── storage         # 存储模块，支持多种选项
│   └─ factory.py   #  └─ 创建/加载存储端点的主要入口
├── utils           # 库中使用的辅助函数
└── vector_stores   # 向量存储模块，包含多种选项
     └─ factory.py  #  └─ 创建向量存储的主要入口
```
在适当的情况下，工厂类提供了注册方法，允许用户提供自己的自定义实现。

## 版本控制

我们使用 [semversioner](https://github.com/raulgomis/semversioner) 来自动化并强制执行发布过程中的语义版本控制。我们的 CI/CD 流水线会检查所有 PR 是否包含由 semversioner 生成的 JSON 文件。提交 PR 时，请运行：
```shell
poetry run semversioner add-change -t patch -d "<描述更改内容的一句话>."
```

# Azurite

一些单元测试和冒烟测试使用 Azurite 来模拟 Azure 资源。可以通过运行以下命令启动：

```sh
./scripts/start-azurite.sh
```

或者，如果已全局安装 Azurite，可以直接在终端运行 `azurite`。有关安装和使用 Azurite 的更多信息，请参阅 [Azurite 文档](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azurite)。

# 生命周期脚本

我们的 Python 包使用 Poetry 管理依赖，并使用 [poethepoet](https://pypi.org/project/poethepoet/) 管理自定义构建脚本。

可用脚本包括：
- `poetry run poe index` - 运行索引 CLI
- `poetry run poe query` - 运行查询 CLI
- `poetry build` - 调用 `poetry build`，将构建 wheel 文件和其他可分发的产物。
- `poetry run poe test` - 执行所有测试。
- `poetry run poe test_unit` - 执行单元测试。
- `poetry run poe test_integration` - 执行集成测试。
- `poetry run poe test_smoke` - 执行冒烟测试。
- `poetry run poe check` - 对包执行一系列静态检查，包括：
  - 格式化
  - 文档格式化
  - 代码检查
  - 安全模式
  - 类型检查
- `poetry run poe fix` - 应用包中可用的自动修复。通常仅限于格式化修复。
- `poetry run poe fix_unsafe` - 应用包中可用的自动修复，包括可能不安全的修复。
- `poetry run poe format` - 在包中显式运行格式化工具。

## 故障排除

### 运行 `poetry install` 时出现 "RuntimeError: llvm-config failed executing, please point LLVM_CONFIG to the path for llvm-config"

确保已安装 llvm-9 和 llvm-9-dev：

`sudo apt-get install llvm-9 llvm-9-dev`

然后在 bashrc 中添加：

`export LLVM_CONFIG=/usr/bin/llvm-config-9`

### 运行 `poetry install` 时出现 "numba/_pymodule.h:6:10: fatal error: Python.h: No such file or directory"

确保已安装 python3.10-dev 或更通用的 `python<version>-dev`：

`sudo apt-get install python3.10-dev`

### LLM 调用持续超过 TPM、RPM 或时间限制

`GRAPHRAG_LLM_THREAD_COUNT` 和 `GRAPHRAG_EMBEDDING_THREAD_COUNT` 默认设置为 50。您可以修改这些值以降低并发性。请参阅 [配置文档](https://microsoft.github.io/graphrag/config/overview/)。