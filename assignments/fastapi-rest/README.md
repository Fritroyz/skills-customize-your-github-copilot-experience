# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small RESTful API using the FastAPI framework to learn routing, request/response models, validation, and basic persistence.

## 📝 Tasks

### 🛠️ Implement API Endpoints

#### Description
Use the provided `starter-code.py` to implement a simple REST API for an `Item` resource. The API should be usable from the terminal (via `curl`) or a browser (OpenAPI docs).

#### Requirements
Completed program should:

- Use FastAPI and Pydantic models for request/response validation.
- Implement the following endpoints:
  - `GET /items` — return a list of items.
  - `GET /items/{item_id}` — return a single item or 404.
  - `POST /items` — create an item and return 201.
  - `PUT /items/{item_id}` — update an existing item.
  - `DELETE /items/{item_id}` — delete an item.
- Validate input and return appropriate HTTP status codes and error messages.
- Keep a simple in-memory store (Python list/dict) in `starter-code.py` so the API is runnable without external services.
- Include brief docstrings and example `curl` requests in comments or the README.

### 🛠️ Optional Extensions

#### Description
Add one or more optional features to make the API more production-like or to explore FastAPI features.

#### Suggestions

- Add JWT-based authentication for write endpoints.
- Persist data using SQLite (e.g., with SQLModel or SQLAlchemy).
- Add pagination, filtering, or search for `GET /items`.
- Add automated tests using `pytest` and `httpx` or `fastapi.testclient`.
- Provide a `Dockerfile` and a `docker-compose.yml` for local development.

#### Notes

- Starter file: `starter-code.py` is provided.
- Install dependencies via `pip install -r requirements.txt`.
- Run locally with the command shown below.

## 📁 Starter Files

- `starter-code.py` — minimal FastAPI app with an in-memory store and example endpoints.
- `requirements.txt` — Python dependencies to install.

## ▶️ Run

Run the API locally with:

```bash
pip install -r assignments/fastapi-rest/requirements.txt
uvicorn assignments.fastapi-rest.starter-code:app --reload --port 8000
```

Open the interactive docs at `http://127.0.0.1:8000/docs`.

Good luck — build something you can test with `curl` or the OpenAPI UI! 🚀
