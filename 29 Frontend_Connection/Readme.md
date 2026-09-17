#
Important: Enable CORS in FastAPI

Your frontend runs separately from your backend, so your FastAPI application needs CORS configuration.

Install nothing extra because FastAPI includes the required Starlette functionality.

In your app/main.py, add this import:

from fastapi.middleware.cors import CORSMiddleware

After creating your FastAPI application, add:

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

Why? Your frontend may run on port 5500, while FastAPI runs on port 8000. CORS allows the browser to make requests between these different origins.

For local practice, this configuration is sufficient. For production, restrict the allowed origins to your actual frontend domain.
