import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def list_gemini_models():
    """Lists all available Gemini models and their supported methods."""
    gemini_api_key = "AIzaSyDB-529s5d0HvqdOkC0QCK0H9lvSk0_8Gc"
    
    if not gemini_api_key:
        print("Error: GEMINI_API_KEY environment variable not set.")
        print("Please ensure you have a .env file in the same directory with GEMINI_API_KEY='YOUR_API_KEY'.")
        return

    try:
        genai.configure(api_key=gemini_api_key)
        print("\n--- Listing ALL Available Gemini Models ---")
        print("Looking for models that support 'generateContent'...")
        print("-" * 50)

        found_suitable_model = False
        for m in genai.list_models():
            # Print full details for debugging
            print(f"Model Name: {m.name}")
            print(f"  Display Name: {m.display_name}")
            print(f"  Description: {m.description}")
            print(f"  Supported Methods: {m.supported_generation_methods}")
            print("-" * 50)

            if 'generateContent' in m.supported_generation_methods:
                if 'gemini-pro' in m.name.lower() or 'gemini-1.0-pro' in m.name.lower():
                    print(f"*** Found a suitable 'gemini-pro' variant: {m.name} ***")
                    found_suitable_model = True
        
        if not found_suitable_model:
            print("\nWARNING: No 'gemini-pro' or 'gemini-1.0-pro' variant found that supports 'generateContent'.")
            print("This might indicate an issue with your API key's permissions or regional access.")
            print("Consider generating a new API key or checking your Google Cloud project settings.")
        
        print("\n--- End of Model Listing ---")

    except Exception as e:
        print(f"An error occurred while listing models: {e}")
        print("Please ensure your API key is valid and has access to the Generative Language API.")

if __name__ == "__main__":
    list_gemini_models()
