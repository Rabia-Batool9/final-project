from fastapi import FastAPI

# The application has no custom configuration, middleware, dependencies, or
# external services; FastAPI's default Swagger UI and ReDoc routes are enabled.
app = FastAPI()

@app.get("/")
def home():
    """Return a simple availability message.

    HTTP method: ``GET``
    Route: ``/``

    This public endpoint accepts no path, query, or request-body parameters.
    It returns a JSON object containing a greeting message with a successful
    ``200 OK`` response. FastAPI may return validation errors for malformed
    requests before this handler is reached.
    """
    return {"message": "Hello, FastAPI!"}
