import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_review_assignment():
    response = client.post("/review", json={
        "assignment_description": "A simple print assignment",
        "github_repo_url": "https://api.github.com/repos/user/repo",
        "candidate_level": "Junior"
    })
    
    assert response.status_code == 200
    assert "found_files" in response.json()
    assert "downsides_comments" in response.json()
    assert "rating" in response.json()
    assert "conclusion" in response.json()

def test_review_assignment_invalid_url():
    response = client.post("/review", json={
        "assignment_description": "A simple print assignment",
        "github_repo_url": "invalid_url",
        "candidate_level": "Junior"
    })
    
    assert response.status_code == 422  