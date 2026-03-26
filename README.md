Agentic-Orchestrator: Multi-Model Autonomous Framework

A production-ready **Agentic AI** framework leveraging the **ReAct (Reason + Act)** pattern. This project demonstrates a sophisticated decoupled architecture, separating core reasoning logic from API delivery and the presentation layer. It is designed for real-time, multi-turn autonomous reasoning with integrated tool invocation.

---

## System Architecture

The system is built using a **Three-Tier Micro-Architecture** to ensure scalability, maintainability, and modularity:

1. **Orchestration Layer (LangGraph):**  
   Implements a stateful cyclic graph for control flow. The LLM can autonomously decide between direct reasoning or invoking external tools for data retrieval.

2. **Service Layer (FastAPI):**  
   Provides an asynchronous REST interface, handling request validation, session persistence, and secure communication between the client and the AI engine.

3. **Presentation Layer (Streamlit):**  
   A reactive frontend that streams the agent’s internal state, exposing the **Chain of Thought** and tool invocation logs for full transparency.

---

## Key Features

- **Dynamic Tool-Calling:** Real-time RAG (Retrieval-Augmented Generation) via **Tavily Search API**, no dedicated vector database required.  
- **Provider-Agnostic Inference:** Hot-swappable support for **Llama 3.3 (via Groq)** and **Google Gemini 1.5 Pro**.  
- **Stateful Memory:** Maintains context across complex multi-turn reasoning tasks using LangGraph’s internal state.  
- **Developer-Friendly Design:** Modular structure, secure `.env` configuration, and clean `.gitignore` to prevent environment leakage.

---

## Tech Stack

| Component          | Technology                       |
|-------------------|---------------------------------|
| Logic / Graph      | LangGraph, LangChain             |
| LLM Providers      | Groq (Llama), Google AI (Gemini)|
| Search Engine      | Tavily AI                        |
| API Framework      | FastAPI (Python 3.10+)           |
| UI Framework       | Streamlit                        |

---

## Installation & Development

### 1. Clone and Set Up Environment
```bash
git clone https://github.com/varshinibairishetty/AI_CHATBOT.git
cd AI_CHATBOT
python -m venv venv
# Activate virtual environment
# Windows
venv\Scripts\activate
# Unix/Linux/Mac
source venv/bin/activate
2. Install Dependencies
pip install --upgrade pip
pip install -r requirements.txt
3. Configure Environment Variables

Create a .env file at the project root with your API keys:

GROQ_API_KEY=your_groq_api_key
GEMINI_API_KEY=your_gemini_api_key
TAVILY_API_KEY=your_tavily_api_key
4. Run Services

Start FastAPI Backend:

uvicorn app.main:app --reload

Start Streamlit Frontend:

streamlit run app/ui/main.py
