from pydantic import BaseModel, HttpUrl
from typing import Optional

class ReviewRequest(BaseModel):
    assignment_description: str
    github_repo_url: HttpUrl
    candidate_level: str

class ReviewResponse(BaseModel):
    found_files: list
    downsides_comments: str
    rating: str
    conclusion: str