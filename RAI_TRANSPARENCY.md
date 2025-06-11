<<<<<<< HEAD
# GraphRAG: Responsible AI FAQ 

## What is GraphRAG? 

GraphRAG is an AI-based content interpretation and search capability. Using LLMs, it parses data to create a knowledge graph and answer user questions about a user-provided private dataset. 

## What can GraphRAG do?  

GraphRAG is able to connect information across large volumes of information and use these connections to answer questions that are difficult or impossible to answer using keyword and vector-based search mechanisms. Building on the previous question, provide semi-technical, high-level information on how the system offers functionality for various uses.  This lets a system using GraphRAG to answer questions where the answers span many documents as well as thematic questions such as “what are the top themes in this dataset?.”

## What are GraphRAG’s intended use(s)? 

* GraphRAG is intended to support critical information discovery and analysis use cases where the information required to arrive at a useful insight spans many documents, is noisy, is mixed with mis and/or dis-information, or when the questions users aim to answer are more abstract or thematic than the underlying data can directly answer. 
* GraphRAG is designed to be used in settings where users are already trained on responsible analytic approaches and critical reasoning is expected. GraphRAG is capable of providing high degrees of insight on complex information topics, however human analysis by a domain expert of the answers is needed in order to verify and augment GraphRAG’s generated responses. 
* GraphRAG is intended to be deployed and used with a domain specific corpus of text data. GraphRAG itself does not collect user data, but users are encouraged to verify data privacy policies of the chosen LLM used to configure GraphRAG. 

## How was GraphRAG evaluated? What metrics are used to measure performance? 

GraphRAG has been evaluated in multiple ways.  The primary concerns are 1) accurate representation of the data set, 2) providing transparency and  groundedness of responses, 3) resilience to prompt and data corpus injection attacks, and 4) low hallucination rates.  Details on how each of these has been evaluated is outlined below by number. 

1) Accurate representation of the dataset has been tested by both manual inspection and automated testing against a “gold answer” that is created from randomly selected subsets of a test corpus. 

2) Transparency and groundedness of responses is tested via automated answer coverage evaluation and human inspection of the underlying context returned.  

3) We test both user prompt injection attacks (“jailbreaks”) and cross prompt injection attacks (“data attacks”) using manual and semi-automated techniques. 

4) Hallucination rates are evaluated using claim coverage metrics, manual inspection of answer and source, and adversarial attacks to attempt a forced hallucination through adversarial and exceptionally challenging datasets. 

## What are the limitations of GraphRAG? How can users minimize the impact of GraphRAG’s limitations when using the system? 

GraphRAG depends on a well-constructed indexing examples.  For general applications (e.g. content oriented around people, places, organizations, things, etc.) we provide example indexing prompts. For unique datasets effective indexing can depend on proper identification of domain-specific concepts.   

Indexing is a relatively expensive operation; a best practice to mitigate indexing is to create a small test dataset in the target domain to ensure indexer performance prior to large indexing operations. 

## What operational factors and settings allow for effective and responsible use of GraphRAG? 

GraphRAG is designed for use by users with domain sophistication and experience working through difficult information challenges.  While the approach is generally robust to injection attacks and identifying conflicting sources of information, the system is designed for trusted users. Proper human analysis of responses is important to generate reliable insights, and the provenance of information should be traced to ensure human agreement with the inferences made as part of the answer generation. 

GraphRAG yields the most effective results on natural language text data that is collectively focused on an overall topic or theme, and that is entity rich – entities being people, places, things, or objects that can be uniquely identified. 

While GraphRAG has been evaluated for its resilience to prompt and data corpus injection attacks, and has been probed for specific types of harms, the LLM that the user configures with GraphRAG may produce inappropriate or offensive content, which may make it inappropriate to deploy for sensitive contexts without additional mitigations that are specific to the use case and model. Developers should assess outputs for their context and use available safety classifiers, model specific safety filters and features (such as https://azure.microsoft.com/en-us/products/ai-services/ai-content-safety), or custom solutions appropriate for their use case. 
=======
# GraphRAG：负责任人工智能常见问题解答

## 什么是 GraphRAG？

GraphRAG 是一种基于人工智能的内容解释和搜索功能。它利用大型语言模型（LLM）解析数据，创建知识图谱，并回答用户关于用户提供的私有数据集的问题。

## GraphRAG 能做什么？

GraphRAG 能够连接大量信息中的关联，并利用这些关联回答使用关键词和基于向量的搜索机制难以或无法回答的问题。在前述问题的基础上，提供半技术性、高层次的信息，说明系统如何为各种用途提供功能。这使得使用 GraphRAG 的系统能够回答跨越多个文档的问题，以及诸如“这个数据集中的主要主题是什么？”之类的主题性问题。

## GraphRAG 的预期用途是什么？

* GraphRAG 旨在支持关键信息发现和分析用例，其中得出有用见解所需的信息跨越多个文档、存在噪声、混合了错误信息或虚假信息，或者用户希望回答的问题比底层数据能直接回答的更加抽象或主题化。
* GraphRAG 设计用于用户已经接受过负责任的分析方法培训且预期进行批判性推理的场景。GraphRAG 能够为复杂信息主题提供高度的洞察力，然而，领域专家对答案的人工分析是必要的，以验证和补充 GraphRAG 生成的响应。
* GraphRAG 旨在与特定领域的文本数据语料库一起部署和使用。GraphRAG 本身不收集用户数据，但鼓励用户验证所选用于配置 GraphRAG 的大型语言模型的数据隐私政策。

## GraphRAG 如何评估？使用哪些指标来衡量性能？

GraphRAG 已通过多种方式进行评估。主要关注点包括：1) 数据集的准确表示，2) 响应的透明性和依据性，3) 对提示和数据语料库注入攻击的鲁棒性，以及 4) 低幻觉率。以下按编号概述了每项的评估细节。

1) 数据集的准确表示通过人工检查和针对测试语料库中随机选择的子集创建的“金标准答案”进行自动化测试。
2) 响应的透明性和依据性通过自动化的答案覆盖评估和对返回的底层上下文的人工检查进行测试。
3) 我们使用人工和半自动化技术测试用户提示注入攻击（“越狱”）和跨提示注入攻击（“数据攻击”）。
4) 幻觉率通过声明覆盖率指标、答案和来源的人工检查以及通过对抗性和极具挑战性的数据集尝试强制幻觉的对抗攻击进行评估。

## GraphRAG 的局限性是什么？用户如何在使用系统时最大程度减少这些局限性的影响？

GraphRAG 依赖于良好构建的索引示例。对于通用应用（例如，围绕人物、地点、组织、事物等的内容），我们提供了示例索引提示。对于独特的数据集，有效索引可能依赖于正确识别特定领域的概念。

索引是一项相对昂贵的操作；减轻索引影响的最佳实践是在目标领域创建一个小型测试数据集，以确保在进行大型索引操作之前索引器的性能。

## 哪些操作因素和设置可以实现 GraphRAG 的有效且负责任的使用？

GraphRAG 设计用于具有领域专业知识和处理复杂信息挑战经验的用户。虽然该方法对注入攻击和识别冲突信息源通常具有鲁棒性，但系统是为可信用户设计的。对响应的适当人工分析对于生成可靠的见解非常重要，应追溯信息的来源，以确保人类对答案生成过程中所做推断的同意。

GraphRAG 在专注于整体主题或主题的自然语言文本数据上效果最佳，并且这些数据富含实体——实体是指可以唯一标识的人物、地点、事物或对象。

虽然 GraphRAG 已针对提示和数据语料库注入攻击的鲁棒性进行了评估，并针对特定类型的危害进行了探测，但用户配置 GraphRAG 的大型语言模型可能会产生不适当或冒犯性的内容，这可能使其在没有针对特定用例和模型的额外缓解措施的情况下，不适合在敏感环境中部署。开发者应根据其上下文评估输出，并使用可用的安全分类器、模型特定的安全过滤器和功能（例如 https://azure.microsoft.com/en-us/products/ai-services/ai-content-safety），或适合其用例的定制解决方案。
>>>>>>> origin
