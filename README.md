# Devops-Assignment-3

# FastAPI Project

This is a simple FastAPI project showcasing CRUD operations with an in-memory database. The project includes API endpoints to create, read, and search for items.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Running Tests](#running-tests)
- [Docker](#docker)
- [GitHub Actions](#github-actions)

## Installation

To run this project locally, you need to have Python and pip installed. Clone the repository and install the dependencies:

bash
git clone https://github.com/talha915/Devops-Assignment-3
cd Devops-Assignment-3
pip install -r requirements.txt

## Usage

Run the FastAPI application:

```bash
uvicorn app.index:app --host 0.0.0.0 --port 8000

## API Endpoints

- GET /: Hello message from FastAPI.
- POST /items/: Create a new item.
- GET /items/{item_id}: Search for an item by ID.
