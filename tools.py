from datetime import datetime
from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun, WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

# ---------- Search Tool ----------

_search = DuckDuckGoSearchRun()

@tool
def search_tool(query: str) -> str:
    """Search the web for current information."""
    return _search.run(query)


# ---------- Wikipedia Tool ----------

_api = WikipediaAPIWrapper(
    top_k_results=1,
    doc_content_chars_max=300
)
_wiki = WikipediaQueryRun(api_wrapper=_api)

@tool
def wiki_tool(query: str) -> str:
    """Fetch background information from Wikipedia."""
    return _wiki.run(query)


# ---------- Save Tool ----------

@tool
def save_tool(data: str) -> str:
    """Save research output to a text file."""
    filename = "research_output.txt"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"\n--- Research Output ({timestamp}) ---\n")
        f.write(data)
        f.write("\n")

    return f"Saved to {filename}"
