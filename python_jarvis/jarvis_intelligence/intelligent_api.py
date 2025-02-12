import requests
import pyttsx3
from bs4 import BeautifulSoup
from serpapi import GoogleSearch

SERP_API_KEY = "607a9a718299594d59d630800ae05ce5d372de168130b86232fd9de94f65daf4"

# Initialize Text-to-Speech
engine = pyttsx3.init()

# Set Female Voice
voices = engine.getProperty('voices')
for voice in voices:
    if "female" in voice.name.lower() or "zira" in voice.name.lower():  
        engine.setProperty('voice', voice.id)
        break

def fetch_google_answer(query):
    """Fetches answer from Google using SERPAPI"""
    params = {
        "q": query,
        "api_key": SERP_API_KEY,
        "num": 3  # Get top 3 search results
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    # Extracting first result snippet
    if "organic_results" in results:
        for result in results["organic_results"]:
            snippet = result.get("snippet", None)
            if snippet:
                return snippet  # Return first snippet found
    
    return "I couldn't find a good answer on Google."

def ask_google_question():
    """Continuously takes user input and fetches an answer from Google"""
    while True:
        question = input("\nAsk me a question (or type 'exit' to stop): ").strip()
        
        if question.lower() == "exit":
            print("Goodbye! 😊")
            break  # Exit the loop if user types 'exit'
        
        answer = fetch_google_answer(question)
        
        print(f"Answer: {answer}")

        # Convert text answer to speech (Female Voice)
        engine.say(answer)
        engine.runAndWait()

# Run the assistant
ask_google_question()
