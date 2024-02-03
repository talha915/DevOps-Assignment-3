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


- git clone https://github.com/talha915/Devops-Assignment-3
- cd Devops-Assignment-3
- pip install -r requirements.txt

## Usage

Run the FastAPI application:


- uvicorn app.index:app --host 0.0.0.0 --port 8000

## API Endpoints

- GET /: Hello message from FastAPI.
- POST /items/: Create a new item.
- GET /items/{item_id}: Search for an item by ID.

## Running Tests
Run the tests using pytest:
- pytest

## Docker
Build the Docker image and run the container:
- docker build -t your-docker-image-name .
- docker run -p 8000:8000 your-docker-image-name

The FastAPI application will be accessible at http://localhost:8000.

## GitHub Actions

This project is configured with GitHub Actions for Continuous Integration (CI) and Continuous Deployment (CD). The workflow includes:

- Set up job
- Run actions/checkout@v3
- Set up Python 3.10
- Installing dependencies.
- Lint with flake8
- Running pytest for testing.
- Building a Docker image.
- Log in to Docker Hub
- Push Docker Image to Docker Hub
- Post Log in to Docker Hub
- Post Set up Python 3.10
- Run actions/checkout@v3
- Complete Job

The CI workflow is triggered on every push or pull request to the main branch.