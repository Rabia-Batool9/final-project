# FastAPI Greeting API

A small university-level FastAPI project with one public endpoint that confirms
the server is running.

## Features

- FastAPI application served by Uvicorn
- Public `GET /` greeting endpoint
- Built-in interactive Swagger UI and ReDoc documentation

## Installation

Create a virtual environment and install the declared runtime dependencies:

```powershell
python -m venv env
.\env\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run the Server

```powershell
uvicorn main:app --reload
```

Visit `http://127.0.0.1:8000/` after the server starts.

## Run with Docker

Build the image from the project root:

```powershell
docker build -t fastapi-greeting-api .
```

Start a container and publish its port 8000 to your computer:

```powershell
docker run --rm -p 8000:8000 fastapi-greeting-api
```

The API, Swagger UI, and ReDoc are then available at the same local addresses
as the direct Uvicorn run. Stop the foreground container with `Ctrl+C`.

## API Documentation

- Interactive Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`
- Full project documentation: [API_DOCUMENTATION.md](API_DOCUMENTATION.md)

## Example Usage

```powershell
curl http://127.0.0.1:8000/
```

Expected response:

```json
{
  "message": "Hello, FastAPI!"
}
```

## Project Structure

The Docker configuration is provided by `Dockerfile`, which builds and starts
the API, and `.dockerignore`, which keeps local files out of the image build
context. Runtime packages are declared in `requirements.txt`.

```text
.
├── main.py
├── README.md
└── API_DOCUMENTATION.md
```

## Troubleshooting

- If imports fail, activate `env` and install `fastapi` and `uvicorn`.
- If port 8000 is busy, add `--port 8001` to the Uvicorn command.
- If Docker cannot start, make sure Docker Desktop is running before building
  the image.
- If a URL returns 404, ensure the server is running and use the root route:
  `http://127.0.0.1:8000/`.

See [API_DOCUMENTATION.md](API_DOCUMENTATION.md) for detailed setup, endpoint,
error-handling, and deployment information.


<img width="1372" height="862" alt="image" src="https://github.com/user-attachments/assets/5ab8822e-891d-498b-9fb1-0c7868b686b6" />

RESULT

<img width="588" height="237" alt="image" src="https://github.com/user-attachments/assets/9de1f05a-a5ac-4438-bcf8-9757e4bb9005" />

