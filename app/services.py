# app/services.py
import httpx
from app.config import GITHUB_TOKEN, OPENAI_API_KEY
from app.logger import logger

async def fetch_github_repo_contents(repo_url: str):
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    response = await httpx.get(repo_url, headers=headers)
    
    if response.status_code != 200:
        logger.error(f"Failed to fetch GitHub repo: {response.text}")
        raise Exception("Failed to fetch GitHub repository contents.")
    
    return response.json()

async def analyze_code_with_openai(code: str, assignment_description: str, candidate_level: str):
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "gpt-4-turbo",
        "messages": [
            {"role": "user", "content": f"Analyze the following code for the assignment: {assignment_description}. Candidate level: {candidate_level}. Code: {code}"}
        ]
    }
    
    response = await httpx.post("https://api.openai.com/v1/chat/completions", json=payload, headers=headers)
    
    if response.status_code != 200:
        logger.error(f"OpenAI API error: {response.text}")
        raise Exception("Failed to analyze code with OpenAI.")
    
    return response.json()["choices"][0]["message"]["content"]