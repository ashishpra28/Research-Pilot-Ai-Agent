# Import libraries
from langchain.tools import tool 
from bs4 import BeautifulSoup 
from tavily import TavilyClient 
from dotenv import load_dotenv
from rich import print 
import requests 
import os 

# Load env 
load_dotenv() 

# Create web search tool 
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def web_search(query:str)->str: 
    """
    Perform a web search using Tavily and retrieve relevant,
    up-to-date information from the internet.

    This tool should be used when answering questions that require:
    - Current events or recent news
    - Real-time information
    - Fact verification
    - Company, product, or technology research
    - Documentation lookup
    - Gathering information not contained in the model's knowledge

    Args:
        query: The search query describing the information to find.

    Returns:
        Relevant web search results including titles, URLs, snippets,
        extracted content, and summaries from trusted sources.
    """
    try:
        output = []  
        results = tavily.search(query=query,max_results=3,search_depth="basic")
        for r in results["results"]:
            output.append(f"Title: {r['title']}\nURL:{r['url']}\nContent:{r['content']}")

        for r in results["results"]:
            print(r["url"])

        return "\n\n---------------------------\n\n".join(output)
    except Exception as e:
         return f"Search failed: {str(e)}"


# Create data scrape tool 
@tool
def scrape_data(url:str)->str:
    """
    Scrape and extract content from a webpage using BeautifulSoup.

    Use this tool when detailed information is needed from a specific
    webpage URL obtained through web search results. This tool fetches
    the page and extracts readable text content for further analysis.
    
    Args:
        url: The webpage URL to scrape.

    Returns:
        Cleaned webpage content including title, headings, paragraphs,
        links, and other relevant textual information extracted from
        the page.
    """
    print(f"Scraping: {url}")
    try:
        r = requests.get(url,timeout=8,headers={"User-Agent":"Mozilla/5.0"})
        soup = BeautifulSoup(r.content,"html.parser")   
        for tag in soup(["script","style","nav","footer"]):
            tag.decompose() 
        return soup.get_text(separator=" ",strip=True)[:2000]
    except Exception as e:
        return f"Could not scrape this url: {str(e)}"
    
    
