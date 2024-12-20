# app/main.py
from fastapi import FastAPI, HTTPException
from app.models import ReviewRequest, ReviewResponse
from app.services import fetch_github_repo_contents, analyze_code_with_openai
from app.logger import logger

app = FastAPI()

@app.post("/review", response_model=ReviewResponse)
async def review_assignment(review_request: ReviewRequest):
    try:
        repo_contents = await fetch_github_repo_contents(review_request.github_repo_url)
        
        code_files = [file['path'] for file in repo_contents['tree'] if file['type'] == 'blob']
        
        reviews = []
        for file in code_files:
            code = await httpx.get(f"{review_request.github_repo_url}/contents/{file}")
            review = await analyze_code_with_openai(code.text, review_request.assignment_description, review_request.candidate_level)
            reviews.append(review)
        
       