import sys
import os

# Add the parent directory of `app/` to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.vector_store import VectorStoreBuilder
from src.recommender import SerialRecommender
from config.config import GOOGLE_API_KEY,MODEL_NAME
from utils.logger import get_logger
from utils.custom_exception import CustomException
from dotenv import load_dotenv

load_dotenv()

logger = get_logger(__name__)

class SerialRecommendationPipeline:
    def __init__(self,persist_dir="chroma_db"):
        try:
            logger.info("Pipeline started")
            vector_builder = VectorStoreBuilder(csv_path="", persist_dir=persist_dir)
            retriever = vector_builder.use_chroma_db().as_retriever()
            self.recommender = SerialRecommender(retriever,GOOGLE_API_KEY,MODEL_NAME)
            logger.info("Pipleine intialized sucesfully...")

        except Exception as e:
            logger.error(f"Failed pipeline in initialization{str(e)}")
            raise CustomException("Failed during initialization",e)

    def recommend(self,query):
        try:
            logger.info("Got input query {query}")
            recommendation = self.recommender.get_recommendation(query)
            logger.info("Recommendation generated sucessfully...")
            return recommendation

        except Exception as e:
            logger.error(f"Failed pipeline in recommend{str(e)}")
            raise CustomException("Failed during recommend",e)
