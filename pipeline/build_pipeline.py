import sys
import os

# Add the parent directory of `app/` to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_loader import SerialDataLoader
from src.vector_store import VectorStoreBuilder
from dotenv import load_dotenv
from utils.logger import get_logger
from utils.custom_exception import CustomException


logger = get_logger(__name__)
load_dotenv()

def main():
    logger.info("Pipeline started...")

    loader = SerialDataLoader("data/HindiSerials.csv","data/HindiSerials_updated.csv")
    processed_csv=loader.load_and_process()

    vector_builder= VectorStoreBuilder(processed_csv)
    vector_builder.create_chroma_db()
    
    logger.info("Vector store built")
    logger.info("Pipeline ran successfully...")

if __name__=="__main__":
    main()