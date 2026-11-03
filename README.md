# 🦜🕸️ LangGraph Tutorial: LLM-Powered AI Agents

My hands-on LangGraph projects. Each branch is a self-contained agent with its own code, README, and graph diagram. `main` is the index.

---

## 🗂️ Projects

| Branch | Agent | What it shows |
|--------|-------|---------------|
| [**project/React-Agent-Function-Calling**](https://github.com/HaykSahakyan11/Langgraph_tutorial/tree/project/React-Agent-Function-Calling) | ReAct agent | A Reason + Act loop with native function calling: the LLM picks tools, a `ToolNode` runs them, and the loop continues until no more tool calls are made |
| [**project/reflection-agent**](https://github.com/HaykSahakyan11/Langgraph_tutorial/tree/project/reflection-agent) | Reflection agent | A generate → reflect loop that rewrites a tweet based on its own critique |
| [**project/reflexion-agent**](https://github.com/HaykSahakyan11/Langgraph_tutorial/tree/project/reflexion-agent) | Reflexion agent | Draft → web search → revise with citations, using structured output (Pydantic) and Tavily search |
| [**project/agentic-rag**](https://github.com/HaykSahakyan11/Langgraph_tutorial/tree/project/agentic-rag) | Agentic RAG | Adaptive routing, document grading, web-search fallback, and hallucination/answer checks over a Chroma vector store |

---

## 🧠 Concepts Covered

- **State graphs**: `StateGraph`, `MessagesState`, custom `TypedDict` state, and reducers
- **Control flow**: conditional edges, loops, conditional entry points, and iteration limits
- **Tool use**: function calling, `ToolNode`, and Tavily web search
- **Structured output**: Pydantic schemas with `bind_tools` and `with_structured_output`
- **Self-improvement**: reflection, Reflexion, and Self-RAG grading loops
- **RAG**: ingestion, chunking, embeddings, Chroma retrieval, and LLM-based graders
- **Testing**: pytest tests for the LLM chains (Agentic RAG branch)

---

## ⚡ Quick Start

Requirements: Python 3.11+ and [uv](https://docs.astral.sh/uv/).

```bash
# 1. Clone
git clone https://github.com/HaykSahakyan11/Langgraph_tutorial.git
cd Langgraph_tutorial

# 2. Pick a project branch
git checkout project/agentic-rag   # for example

# 3. Install dependencies
uv sync

# 4. Add your API keys
cp .env.example .env   # if the branch has one; otherwise create .env

# 5. Run
uv run main.py
```

Keys used across the projects:

```env
OPENAI_API_KEY=...       # all projects
TAVILY_API_KEY=...       # Reflexion agent, Agentic RAG, ReAct agent
LANGSMITH_TRACING=true   # optional: LangSmith tracing
LANGSMITH_API_KEY=...    # optional
```

Each branch's README has the exact setup and run steps for that agent.

---

## 👤 Author

**Hayk Sahakyan**. GitHub: [@HaykSahakyan11](https://github.com/HaykSahakyan11)

---

## 📚 Resources

- [LangGraph course on Udemy](https://www.udemy.com/course/langgraph/) by Eden Marco, which these projects follow ([course repo](https://github.com/emarco177/langgraph-course))
- [LangGraph documentation and tutorials](https://langchain-ai.github.io/langgraph/)
- [LangChain](https://github.com/langchain-ai/langchain)

---

## 📄 License

Apache License 2.0. See [LICENSE.txt](LICENSE.txt).
