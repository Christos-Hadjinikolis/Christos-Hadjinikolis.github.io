# RL, RAG, And LLM Fine-Tuning Learning Plan

Private development plan. This file is intentionally stored under `_internal/` and must not be published as a site page.

Created: 2026-04-11

## Purpose

Build a practical foundation in three related areas:

- reinforcement learning, especially the concepts behind sequential decision-making and RLHF/RFT
- retrieval-augmented generation, especially retrieval quality, grounding, and evaluation
- LLM fine-tuning, especially when to fine-tune, how to prepare data, and how to evaluate results

This is not a certificate-chasing plan. The goal is operational understanding: enough theory to reason clearly and enough implementation exposure to make good engineering decisions.

## Phase 1: Orientation

- [ ] Read OpenAI Spinning Up: [Introduction](https://spinningup.openai.com/en/latest/user/introduction.html)
- [ ] Read OpenAI Spinning Up: [Key Concepts in RL](https://spinningup.openai.com/en/latest/spinningup/rl_intro.html)
- [ ] Watch DeepMind: [David Silver RL Lecture 1](https://www.youtube.com/watch?v=2pWv7GOvuf0)
- [ ] Watch Stanford Online: [CS234 2024 Lecture 1](https://www.youtube.com/watch?v=WsvFL-LjA6U)
- [ ] Write a one-page note explaining: agent, state, action, reward, policy, value function, exploration vs exploitation

## Phase 2: Practical RL Basics

- [ ] Skim Hugging Face Deep RL Course: [Unit 0](https://huggingface.co/learn/deep-rl-course/unit0/introduction)
- [ ] Complete Hugging Face Deep RL Course: Unit 1, introduction to deep reinforcement learning
- [ ] Complete Hugging Face Deep RL Course: Unit 2, Q-learning
- [ ] Optional: read Sutton and Barto, *Reinforcement Learning: An Introduction*, Chapter 1 and Chapter 3
- [ ] Build a small tabular Q-learning notebook and keep it under `_internal/learning/notebooks/` if useful

## Phase 3: RAG Foundations

- [ ] Read OpenAI Help: [RAG and Semantic Search for GPTs](https://help.openai.com/en/articles/8868588-retrieval-augmented-generation-rag-and-semantic-search-for-gpts)
- [ ] Read LangChain docs: [Build a RAG agent with LangChain](https://docs.langchain.com/oss/python/langchain/rag)
- [ ] Read LlamaIndex docs: [Building RAG from Scratch](https://docs.llamaindex.ai/en/stable/optimizing/building_rag_from_scratch/)
- [ ] Skim the original RAG paper abstract: [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://proceedings.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html)
- [ ] Write a one-page note explaining: indexing, chunking, embeddings, retrievers, rerankers, context assembly, generation, evaluation

## Phase 4: RAG Course Work

- [ ] Start DeepLearning.AI: [Retrieval Augmented Generation (RAG)](https://www.deeplearning.ai/courses/retrieval-augmented-generation-rag/)
- [ ] Complete module on information retrieval and search foundations
- [ ] Complete module on vector databases and chunking
- [ ] Complete module on prompt design and response generation
- [ ] Complete module on RAG evaluation, monitoring, and production concerns
- [ ] Build a tiny RAG prototype over a small set of personal notes or blog drafts

## Phase 5: LLM Fine-Tuning Foundations

- [ ] Read OpenAI docs: [Model optimization](https://platform.openai.com/docs/guides/fine-tuning)
- [ ] Read OpenAI docs: [Supervised fine-tuning](https://platform.openai.com/docs/guides/supervised-fine-tuning)
- [ ] Read OpenAI docs: [Fine-tuning best practices](https://platform.openai.com/docs/guides/fine-tuning-best-practices)
- [ ] Read Hugging Face LLM Course: [Supervised Fine-Tuning](https://huggingface.co/learn/llm-course/chapter11/1)
- [ ] Read Hugging Face PEFT: [LoRA guide](https://huggingface.co/docs/peft/main/en/developer_guides/lora)
- [ ] Write a decision note: prompt engineering vs RAG vs supervised fine-tuning vs reinforcement fine-tuning

## Phase 6: Fine-Tuning Course Work

- [ ] Complete DeepLearning.AI: [Finetuning Large Language Models](https://www.deeplearning.ai/short-courses/finetuning-large-language-models/)
- [ ] Watch the sections on why/when to fine-tune
- [ ] Work through the data preparation section
- [ ] Work through the training and evaluation sections
- [ ] Optional follow-up: DeepLearning.AI [Fine-tuning & RL for LLMs: Intro to Post-training](https://corporate.deeplearning.ai/courses/fine-tuning-and-reinforcement-learning-for-llms-intro-to-post-training/information)

## Phase 7: Integration Notes

- [ ] Explain how RLHF/RFT relates to classical RL without pretending they are the same problem
- [ ] Explain why RAG is often a better first move than fine-tuning for knowledge updates
- [ ] Explain where fine-tuning helps: format, style, task behaviour, compressed examples, and repeated instruction-following failures
- [ ] Explain where fine-tuning is weak: factual freshness, missing retrieval, poor evals, and dirty data
- [ ] Turn the notes into one internal architecture memo: "How I decide between prompting, RAG, SFT, and RFT"

## Review Cadence

- [ ] Revisit this plan monthly
- [ ] Move completed notes into `_internal/learning/notes/`
- [ ] Only promote a resource to the public reading page if it becomes something worth recommending after completing it
