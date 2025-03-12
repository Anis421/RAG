from langchain_community.llms import HuggingFaceHub
from dotenv import load_dotenv
import os

load_dotenv()
hf_token = os.getenv("HUGGINGFACE_TOKEN")

def rag_response(query):
    llm = HuggingFaceHub(
        repo_id = "mistralai/Mixtral-8x7B-Instruct-v0.1",
        huggingfacehub_api_token = hf_token,
    )
    return llm.invoke(query)