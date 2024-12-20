import pytest
from app.services import fetch_github_repo_contents, analyze_code_with_openai
from unittest.mock import patch

@pytest.mark.asyncio
async def test_fetch_github_repo_contents():
    with patch('httpx.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "tree": [
                {"path": "file1.py", "type": "blob"},
                {"path": "file2.py", "type": "blob"}
            ]
        }
        
        repo_contents = await fetch_github_repo_contents("https://api.github.com/repos/user/repo")
        assert len(repo_contents['tree']) == 2
        assert repo_contents['tree'][0]['path'] == "file1.py"

@pytest.mark.asyncio
async def test_analyze_code_with_openai():
    with patch('httpx.post') as mock_post:
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            "choices": [{"message": {"content": "Great job!"}}]
        }
        
        review = await analyze_code_with_openai("print('Hello, World!')", "A simple print assignment", "Junior")
        assert review == "Great job!"