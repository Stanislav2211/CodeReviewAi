# CodeReviewAI

CodeReviewAI is a Coding Assignment Auto-Review Tool that automates the process of reviewing coding assignments using OpenAI's GPT API and the GitHub API.

## Features

- Fetches code from a specified GitHub repository.
- Analyzes the code using OpenAI's GPT-4 Turbo.
- Provides a structured review including found files, comments, rating, and conclusion.

## Requirements

- Python 3.8 or higher
- GitHub API Token
- OpenAI API Key

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/CodeReviewAI.git
   cd CodeReviewAI

2. Create a virtual environment (optional but recommended):
    
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. Install the required packages:
    
    pip install -r requirements.txt
4.Create a .env file in the root directory and add your API keys:

    GITHUB_TOKEN=your_github_token
    OPENAI_API_KEY=your_openai_api_key

5.Run the application
    
    uvicorn app.main:app --reload

PART 2
To architect the Coding Assignment Auto-Review Tool for scalability, I would implement a microservices architecture with a focus on asynchronous processing. Incoming review requests would be queued using a message broker like RabbitMQ or Redis, allowing for efficient handling of 100+ requests per minute. Worker services would process these requests in parallel, utilizing asynchronous I/O to fetch repository contents and analyze code, which is crucial for handling large repositories with 100+ files. For data storage, I would use a scalable database solution like PostgreSQL or MongoDB, with read replicas to distribute load and improve read performance. Caching frequently accessed data with Redis would reduce the number of API calls to GitHub and OpenAI, enhancing response times and minimizing costs. To manage increased usage of the OpenAI and GitHub APIs, I would implement rate limiting and exponential backoff strategies to gracefully handle API limits, along with monitoring tools to track usage patterns and costs. Additionally, I would consider caching responses from the OpenAI API for similar requests to further reduce costs and optimize performance. This architecture would ensure high availability, reliability, and responsiveness under heavy traffic conditions.