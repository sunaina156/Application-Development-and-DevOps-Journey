# Important: Enable CORS in FastAPI

Your frontend runs separately from your backend, so your FastAPI application needs CORS configuration. <br>

Install nothing extra because FastAPI includes the required Starlette functionality. <br> <br>

In your app/main.py, add this import: <br>

```text
from fastapi.middleware.cors import CORSMiddleware
```

 <br>
After creating your FastAPI application, add: <br>

```text
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
```

 <br>
Why? Your frontend may run on port 5500, while FastAPI runs on port 8000. CORS allows the browser to make requests between these different origins. <br>

For local practice, this configuration is sufficient. For production, restrict the allowed origins to your actual frontend domain. <br>

---

# Run your application

**Terminal 1 — Start FastAPI** <br>

From the project root: <br>

```text
uvicorn app.main:app --reload
```

 <br>
Your API should be available at: <br>

```text
http://127.0.0.1:8000
```

 <br> <br>
 
**Terminal 2 — Start the frontend** <br>

If you have VS Code: <br>

Install the Live Server extension. <br>

Open frontend/index.html. <br>

Right-click the file. <br>

Select Open with Live Server. <br>

Your frontend will usually open at: <br>

http://127.0.0.1:5500/frontend/index.html <br>

 <br>
Important limitation in your current backend <br>

Your current POST /urls endpoint uses: <br>

user_id = 1 <br>

Therefore, this frontend will work with your current backend, but every generated URL is associated with user ID 1. <br>

Also, your backend currently does not include authentication in the code you uploaded. We can integrate registration and login after the basic frontend is working.
 <br> <br>
 
Expected flow <br>

```text
User enters URL
       |
       ▼
JavaScript fetch()
       |
       ▼
POST /urls
       |
       ▼
FastAPI generates short code
       |
       ▼
PostgreSQL stores URL
       |
       ▼
FastAPI returns JSON
       |
       ▼
Frontend displays short URL
```

 <br>

 
