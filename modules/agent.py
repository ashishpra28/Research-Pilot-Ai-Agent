# Import libraries
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent 
from langchain_core.output_parsers import StrOutputParser 
from modules.tools import web_search
from modules.prompts import writer_prompt, reviewer_prompt, revision_prompt
from dotenv import load_dotenv
import os 
import os

# Load env 
load_dotenv()

print("GROQ KEY FOUND:", bool(os.getenv("GROQ_API_KEY")))
print("TAVILY KEY FOUND:", bool(os.getenv("TAVILY_API_KEY")))

# Define llm
llm = init_chat_model(model="llama-3.1-8b-instant",
                      model_provider="groq",
                      temperature = 0)

# Define parser 
parser = StrOutputParser()

# 1. Create search agent
def search_agent():
    return create_agent(
        model=llm,
        tools=[web_search]
    )

# Create writer chain 
writer_chain = writer_prompt | llm | parser 

# Create reviewer chain 
reviewer_chain = reviewer_prompt | llm | parser

# Create revision chain
revision_chain = revision_prompt | llm | parser


