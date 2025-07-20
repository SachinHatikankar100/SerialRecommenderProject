import sys
import os

# Add the parent directory of `app/` to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI
from src.prompt_template import get_serial_prompt


class SerialRecommender:
    def __init__(self,retriever,api_key:str,model_name:str):
        self.llm = ChatGoogleGenerativeAI(api_key=api_key,model=model_name,temperature=0)
        self.prompt = get_serial_prompt()


        self.qa_chain = RetrievalQA.from_chain_type(
            llm = self.llm,
            chain_type = "stuff",
            retriever=retriever,
            return_source_documents = True,
            chain_type_kwargs = {"prompt":self.prompt}
        )

    def get_recommendation(self,query:str):
        result = self.qa_chain({"query":query})
        return result['result']