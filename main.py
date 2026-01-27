from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

from tools import search_tool, wiki_tool, save_tool

load_dotenv()


# -------------------------------
# Output Schema
# -------------------------------

class ResearchResponse(BaseModel):
    topic: str
    summary: list[str]
    sources: list[str]
    tools_used: list[str]


# -------------------------------
# LLM (FREE + STABLE)
# -------------------------------

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.2
)

parser = PydanticOutputParser(pydantic_object=ResearchResponse)


# -------------------------------
# Prompt (STRICT + STRUCTURED)
# -------------------------------

prompt = ChatPromptTemplate.from_template(
    """
You are an academic advisor and researcher.

Rules you MUST follow:
- Write the summary as bullet points (5–8 points).
- Be factual and realistic.
- Do NOT invent universities, news, or sources.
- If the question is general (career, concepts), rely on general knowledge.
- If search results are provided, use them strictly.
- Do NOT repeat sentences.
- Keep language simple and professional.

{format_instructions}

Topic:
{query}

Search Results (only if available):
{search_results}

Wikipedia Context (only if available):
{wiki_results}
"""
).partial(format_instructions=parser.get_format_instructions())


# -------------------------------
# Helper: Decide when to search
# -------------------------------

def needs_search(query: str) -> bool:
    keywords = ["current", "latest", "news", "today", "updates", "recent"]
    return any(word in query.lower() for word in keywords)


# -------------------------------
# Main Execution
# -------------------------------

query = input("What can I help you research? ").strip()

use_search = needs_search(query)

search_results = "Not applicable"
wiki_results = "Not applicable"

if use_search:
    search_results = search_tool.invoke(query)
    wiki_results = wiki_tool.invoke(query)

response = llm.invoke(
    prompt.format(
        query=query,
        search_results=search_results,
        wiki_results=wiki_results
    )
)

structured = parser.parse(response.content)

# -------------------------------
# Sources & Tools Used
# -------------------------------

if use_search:
    structured.sources = [
        "DuckDuckGo search results",
        "Wikipedia"
    ]
    structured.tools_used = ["search_tool", "wiki_tool"]
else:
    structured.sources = ["General knowledge"]
    structured.tools_used = ["llm only"]

# -------------------------------
# Save Output
## -------------------------------

formatted_output = f"""Topic: {structured.topic}

Summary:
""" + "\n".join(f"- {point}" for point in structured.summary) + f"""

Sources:
""" + "\n".join(f"- {src}" for src in structured.sources) + f"""

Tools Used:
""" + "\n".join(f"- {tool}" for tool in structured.tools_used)


# Save formatted output
save_tool.invoke(formatted_output)

# Print to console
print("\n========= FINAL OUTPUT =========\n")
print(formatted_output)
