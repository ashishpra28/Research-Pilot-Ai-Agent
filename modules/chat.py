# Import libraries
from langchain_core.prompts import ChatPromptTemplate
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent 
from langchain_core.runnables import RunnableSequence, RunnablePassthrough, RunnableParallel
from dotenv import load_dotenv

# Load env 
load_dotenv()

# Define llm 
llm = init_chat_model(model="openai/gpt-oss-20b",model_provider="groq")

# 
