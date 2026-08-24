# FastAPI Application Documentation

## 1. Project Overview

This is a minimal FastAPI web API that provides a public root endpoint for
checking that the service is running. The endpoint returns a JSON greeting.

## 2. Project Structure

| Path | Purpose |
| --- | --- |
| `main.py` | Defines the FastAPI application instance and the `GET /` endpoint. |
| `requirements.txt` | Declares the FastAPI and Uvicorn runtime dependencies. |
| `Dockerfile` | Builds a container image that runs the API on port 8000. |
| `.dockerignore` | Excludes local-only files from the Docker build context. |
| `API_DOCUMENTATION.md` | Detailed API and setup documentation. |
| `README.md` | Quick-start guide for the project. |

The project currently has no database, templates, static files, authentication,
custom middleware, environment configuration, or external API integrations.

## 3. Installation

Create and activate a virtual environment, then install the declared runtime
packages:

```powershell
python -m venv env
.\env\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

If PowerShell prevents activation, see [Troubleshooting](#14-troubleshooting).

## 4. Running the Application

With the virtual environment activated, start the development server from the
project root:

```powershell
uvicorn main:app --reload
```

The application will normally be available at `http://127.0.0.1:8000`.

## 5. API Endpoints

| Method | Endpoint | Description | Request | Response |
| --- | --- | --- | --- | --- |
| `GET` | `/` | Returns a greeting confirming that the API is reachable. | No parameters or body. | `200 OK` with a message object. |

### `GET /`

- **URL:** `/`
- **HTTP method:** `GET`
- **Purpose:** Provides a simple response from the FastAPI application.
- **Authentication:** None.
- **Parameters:** None (no path parameters, query parameters, headers, or body
  are defined by the application).
- **Request body:** None.

Successful response (`200 OK`):

```json
{
  "message": "Hello, FastAPI!"
}
```

The endpoint has no application-defined error responses. FastAPI can return
standard validation errors (commonly `422 Unprocessable Entity`) if a request
cannot be validated before a route handler runs.

Example request:

```powershell
curl http://127.0.0.1:8000/
```

## 6. Swagger UI and ReDoc

The application is created with FastAPI defaults, so automatic documentation is
enabled while the server is running:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## 7. Request/Response Models

There are no user-defined Pydantic request or response models in this project.
`GET /` returns a plain JSON object with one field:

| Field | Type | Description |
| --- | --- | --- |
| `message` | string | Greeting returned by the root endpoint. |

No explicit FastAPI `response_model` is configured.

## 8. Authentication

Authentication and authorization are not implemented. No login route, token
generation, or authorization header is required.

## 9. Database

No database connection, ORM model, table, or CRUD operation is present.

## 10. Environment Variables

The application does not read environment variables.

| Variable | Purpose | Required | Example |
| --- | --- | --- | --- |
| _None_ | No environment-based configuration is implemented. | No | N/A |

## 11. Error Handling

The application does not define custom exception handlers or explicit HTTP
errors. FastAPI supplies its normal framework responses, including:

| Status | When it can occur |
| --- | --- |
| `404 Not Found` | The requested URL does not match a registered route. |
| `422 Unprocessable Entity` | FastAPI cannot validate a request before invoking a handler. The documented root endpoint has no inputs, so this is unlikely during normal use. |
| `500 Internal Server Error` | An unexpected server-side exception occurs. |

## 12. Testing

Start the server, then test the root endpoint in one of these ways.

**Swagger UI:** Open `http://127.0.0.1:8000/docs`, expand `GET /`, select
**Try it out**, then **Execute**.

**curl:**

```powershell
curl http://127.0.0.1:8000/
```

**Python:**

```python
import requests

response = requests.get("http://127.0.0.1:8000/")
print(response.status_code)
print(response.json())
```

Install `requests` separately if you use the Python example:
`python -m pip install requests`.

## 13. Deployment

The project includes a Dockerfile for a self-contained deployment image. Build
and run it from the project root:

```powershell
docker build -t fastapi-greeting-api .
docker run --rm -p 8000:8000 fastapi-greeting-api
```

The image installs the dependencies from `requirements.txt`, copies the API
source, and starts `uvicorn main:app --host 0.0.0.0 --port 8000`. It exposes
port 8000; `-p 8000:8000` makes it accessible at `http://127.0.0.1:8000`.

For a public deployment, use environment-appropriate process supervision,
HTTPS termination, and logging. The current application requires no environment
variables or database setup.

## 14. Troubleshooting

| Problem | Suggested resolution |
| --- | --- |
| `ModuleNotFoundError` for FastAPI or Uvicorn | Activate `env` and run `python -m pip install -r requirements.txt`. |
| Virtual-environment activation is blocked | In PowerShell, use the appropriate execution-policy setting permitted by your institution or system administrator, then retry `.\env\Scripts\Activate.ps1`. |
| Port 8000 is already in use | Stop the process using that port, or start Uvicorn with another port, for example `uvicorn main:app --reload --port 8001`. |
| `404 Not Found` | Confirm the server is running and request `http://127.0.0.1:8000/` (including the trailing slash). |
| `422 Unprocessable Entity` | Check the endpoint documentation for required inputs. `GET /` defines none. |
| Docker build or run fails | Confirm Docker Desktop is installed and running, then run the Docker commands from the folder containing `Dockerfile`. |
