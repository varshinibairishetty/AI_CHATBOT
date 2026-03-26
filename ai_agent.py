import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from tavily import TavilyClient
from langchain_core.tools import Tool
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage

load_dotenv()

# Setup Tavily Search Tool
tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def tavily_search(query: str) -> str:
    result = tavily_client.search(query)
    return result.get("answer", str(result))

search_tool = Tool(
    name="TavilySearch",
    func=tavily_search,
    description="Search the web for real-time information. Input should be a search string."
)

def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    # 1. Initialize the LLM
    if provider.lower() == "groq":
        llm = ChatGroq(model=llm_id, api_key=os.getenv("GROQ_API_KEY"))
    elif provider.lower() == "gemini":
        llm = ChatGoogleGenerativeAI(model=llm_id, google_api_key=os.getenv("GEMINI_API_KEY"))
    else:
        raise ValueError("Provider not supported")

    # 2. Setup Tools
    tools = [search_tool] if allow_search else []

    # 3. Bind Tools to the LLM (This prevents the 400 error)
    if tools:
        llm = llm.bind_tools(tools)

    # 4. Create the Agent
    agent = create_react_agent(
        model=llm,
        tools=tools,
        prompt=system_prompt
    )

    # 5. Execute and Return
    state = {"messages": [HumanMessage(content=query)]}
    response = agent.invoke(state)
    return response["messages"][-1].content