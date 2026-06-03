# Import libraries
import re
from modules.agent import search_agent, writer_chain, reviewer_chain, revision_chain 
from modules.tools import scrape_data
from dotenv import load_dotenv 
load_dotenv()

# Create research pipeline
def research_pipeline(topic:str)->dict: 

    state = {}

    # 1. Search agent
    print("\n"+"="*50)
    print("STEP 1 - Search Agent Working...")
    print("="*50)

    search = search_agent() 
    search_results = search.invoke({
        "messages": [("user",f"""
                      Find recent, reliable and detailed information about: {topic}"
                      """ )]
    })

    tool_content = ""

    for msg in search_results["messages"]:
        if msg.__class__.__name__ == "ToolMessage":
            tool_content = msg.content
            break

    state["search_results"] = tool_content

    urls = re.findall(r'https?://[^\s]+',state["search_results"])

    blocked_domains = ["youtube.com","instagram.com","facebook.com","reddit.com","x.com","twitter.com"]   
    
    clean_urls = []
    for url in urls:
         if not any(domain in url for domain in blocked_domains):
            clean_urls.append(url)
    
    state["urls"] = clean_urls 
    

    # 2. Scrape data
    print("\n"+"="*50)
    print("STEP 2 - Scraping URLs...")
    print("="*50)

    sources = []
    
    for url in state["urls"]:
        print(f"Scraping URL - {url}")
        content = scrape_data.invoke(url)

        if "Could not scrape" not in content:
            sources.append({
                "url":url,
                "content":content
            })
        
    state["sources"] = sources
    state["scraped_content"] = "\n\n".join(source["content"] for source in sources)

    print("\nTotal Sources Scraped:", len(sources))
    print("\nResearch Corpus Length:", len(state["scraped_content"]))
    print(len(state["sources"]))


    # 3. Writer Chain
    print("\n" + "=" * 50)
    print("STEP 3 - Writer is drafting the report...")
    print("=" * 50)

    research = ""

    for source in state["sources"]:
        research+=(
            f"\n\nURL: {source['url']}\n\n"
            f"{source['content'][:1500]}"
        )

    state["research_corpus"] = research 
    
    state["report"] = writer_chain.invoke({
        "topic":topic,
        "research":state["research_corpus"]
    })

    print(state["report"])
    print("\nReport Length:", len(state["report"]))


    # 4. Reviewer chain
    print("\n" + "=" * 50)
    print("STEP 4 - Reviewer is reviewing the report...")
    print("=" * 50)

    state["feedback"] = reviewer_chain.invoke({
        "report":state["report"]
    })

    print(state["feedback"])


    # 5. Revision Chain
    print("\n" + "=" * 50)
    print("STEP 5 - Rebuilding the report according to feedback...")
    print("=" * 50)

    state["revised_report"] = revision_chain.invoke({
        "report":state["report"],
        "feedback":state["feedback"]
    })

    print(state["revised_report"])

    return state

if __name__ == "__main__":
    topic = input("Enter a research topic: ")
    research_pipeline(topic)