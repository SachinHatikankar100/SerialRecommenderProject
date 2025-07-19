from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq
from src.prompt_template import get_serial_prompt


class SerialRecommender:
    def __init__(self,retriever,model_name:str,api_key:str):
        self.llm = ChatGroq(model=model_name,api_key=api_key,temperature=0)
        self.prompt = get_serial_prompt()


        self.qa_chain = RetrievalQA.from_chain_type(
            llm = self.llm,
            chain_type = "stuff",
            retriever=retriever,
            return_source_document = True,
            chain_type_kwargs = {"prompt":self.prompt}
        )

    def getRecommendation(self,query:str):
        result = self.qa_chain({"query":query})
        return result['result']