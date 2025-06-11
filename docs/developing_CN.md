# 开发指南

# 要求

| 名称                | 安装方式                                                     | 用途                                                                               |
| ------------------- | ------------------------------------------------------------ | --------------------------------------------------------------------------------- |
| Python 3.10-3.12    | [下载](https://www.python.org/downloads/)                    | 该库基于 Python 开发。                                                            |
| Poetry              | [安装说明](https://python-poetry.org/docs/#installation)     | Poetry 用于管理 Python 代码库中的包和虚拟环境。                                    |

# 入门

## 安装依赖

```sh
# 安装 Python 依赖。
poetry install
```

## 执行索引引擎

```sh
poetry run poe index <...args>
```

## 执行查询

```sh
poetry run poe query <...args>
```

# Azurite

一些单元测试和冒烟测试使用 Azurite 来模拟 Azure 资源。可以通过运行以下命令启动：

```sh
./scripts/start-azurite.sh
```

或者如果已全局安装 Azurite，可以直接在终端运行 `azurite`。有关如何安装和使用 Azurite 的更多信息，请参阅 [Azurite 文档](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azurite)。

# 生命周期脚本

我们的 Python 包使用 Poetry 管理依赖，并使用 [poethepoet](https://pypi.org/project/poethepoet/) 管理构建脚本。

可用脚本包括：

- `poetry run poe index` - 运行索引 CLI
- `poetry run poe query` - 运行查询 CLI
- `poetry build` - 调用 `poetry build`，将构建一个 wheel 文件和其他可分发的工件。
- `poetry run poe test` - 执行所有测试。
- `poetry run poe test_unit` - 执行单元测试。
- `poetry run poe test_integration` - 执行集成测试。
- `poetry run poe test_smoke` - 执行冒烟测试。
- `poetry run poe test_verbs` - 执行基本工作流程的测试。
- `poetry run poe check` - 对包执行一系列静态检查，包括：
  - 格式化
  - 文档格式化
  - 代码检查（linting）
  - 安全模式检查
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

### LLM 调用不断超过 TPM、RPM 或时间限制

`GRAPHRAG_LLM_THREAD_COUNT` 和 `GRAPHRAG_EMBEDDING_THREAD_COUNT` 默认值均为 50。您可以修改这些值以减少并发性。请参阅 [配置文档](config/overview.md)。