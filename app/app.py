import sys
import os

# Add the parent directory of `app/` to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from pipeline.pipeline import SerialRecommendationPipeline
from dotenv import load_dotenv

st.set_page_config(page_title="Serial Recommender", layout="wide")

load_dotenv()


@st.cache_resource
def init_pipeline():
    return SerialRecommendationPipeline()

pipeline = init_pipeline()

st.title("Serial Recommender")

query = st.text_input("Give your input: E.g: Suggest a serial like kyuki saas bhi kabhi bahu thi...")

if query:
    with st.spinner("Fetching recommendations for you..."):
            response = pipeline.recommend(query)
            st.markdown("*****Recommendations*****")
            st.write(response)
