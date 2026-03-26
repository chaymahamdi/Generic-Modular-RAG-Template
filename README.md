# Generic Modular RAG Template

This project implements a Retrieval-Augmented Generation (RAG) system using **PostgreSQL** with the **pgvector** extension as a vector database.

## About the Project

This is a **FastAPI-based project** designed to build a **generic and modular RAG pipeline**.

The goal is not only to build a working system, but also to:

- Experiment with different RAG strategies  
- Compare parsing, chunking, embedding, and retrieval approaches  
- Apply clean software engineering design patterns  
- Explore how pgvector works (indexes, similarity search, etc.) 

## Getting Started
### Prerequisites

Make sure you have the following installed:

- **Python 3.14.14**
- **Docker & Docker Compose**

### Installation

**Clone the repository**
```bash
git clone https://github.com/chaymahamdi/Generic-Modular-RAG-Template.git
```
**Create and Activate a Virtual Environment**

```bash
python3 -m venv .venv
source .venv/bin/activate
```
**Install Dependencies**
```bash
pip install -r requirements.txt
```
4. Start required services

You can start the infrastructure using Docker Compose:
```bash
docker-compose up --build
```
This will start:

- PostgreSQL with pgvector (vector database)
- Liquibase (for database schema management)

## Current Status

🚧 This project is still in progress.

For now, I have:

- Designed the project architecture
- Implemented the document ingestion pipeline
- Integrated PDF parsing using pymupdf4llm
## Next Steps
- Add document chunking strategies
- Generate and store embeddings
- Implement semantic search using pgvector
- Integrate an LLM for question answering
