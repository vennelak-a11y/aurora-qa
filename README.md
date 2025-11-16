Aurora Question-Answering Service

This project is a lightweight question-answering API that extracts answers from member messages provided by the public Aurora API.
It accepts a natural-language question and returns a concise answer based solely on user messages.

Overview:

This service exposes a single endpoint:

GET /ask question=Your+question+here

The API takes any natural-language query (e.g., “When is Layla planning her trip to London?”) and searches through message history returned by the Aurora public /messages endpoint. It then extracts the most relevant answer and returns it in this format:

{ "answer": "..." }


The project uses:

FastAPI for the web service

OpenAI GPT model for semantic reasoning

HTTPX for fetching messages

JSON-based retrieval (no database needed)

How It Works:

Fetch Messages
The service calls the public endpoint:

GET /messages

and loads all member messages into memory.

Provide Context to the LLM
Messages are converted into a structured list the model can understand.

Ask the Model to Answer
The user’s question + message context is passed to the OpenAI reasoning model with instructions to extract an answer only if the dataset contains one.

Return a Clean JSON Response
The API returns:

{ "answer": "..." }


Design Notes (Bonus Requirement):
Why this design?

This system is intentionally simple, fast, and deployable. It avoids databases, indexing, or heavy infrastructure to match the project’s scope.

Approach Considered:
1. LLM-Only Retrieval (Chosen Approach)

Fetch messages

Give them as context to the model

Ask the model to find the answer

Fast to build and works well for small datasets
Tradeoff: Not efficient for millions of messages.

2. Embedding + Vector Search

Convert each message into an embedding

Store them in a vector store like FAISS

Retrieve top-k similar messages
Pros: Scales well
Cons: Requires more setup and indexing

3. Rule-Based Keyword Matching

Search messages with regex / filters

Very fast
Cons: Fails for natural language questions and synonyms

Final Decision:
Approach #1 provides the best balance of simplicity, accuracy, and ease of deployment given the project requirements.

Running the App Locally:

Install dependencies:

pip install -r requirements.txt

Run the server:

uvicorn app:app --reload

Visit:

http://localhost:8000/docs

File Structure:
aurora-qa/
│
├── app.py
├── requirements.txt
└── README.md

Deployment:

You can deploy this service publicly using:

Render

Railway.app

Deta Space

Fly.io

Vercel (via serverless Python)

All require only:

app.py

requirements.txt

Example Query:
ask question=What are Amira’s favorite restaurants?

Example response:
{ "answer": "There is no message mentioning Amira’s favorite restaurants." }

Submission:
This repository includes:
Working API
Deployed endpoint
README with design notes
Clean, minimal code
