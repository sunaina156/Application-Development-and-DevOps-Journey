# Add the imports
import random
import string

from fastapi import FastAPI, HTTPException, status

from db import get_connection
from models import URLCreate

# Create the FastAPI application:

app = FastAPI(
    title="URL Shortener API",
    description="A practice URL shortening API using FastAPI and PostgreSQL",
    version="1.0.0"
)

# Add the short_cod_generator
def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits

    code = ""

    for _ in range(length):
        code += random.choice(characters)

    return code

# Create a function to generate a unique short code

def generate_unique_short_code(cursor):
    while True:
        short_code = generate_short_code()

        cursor.execute(
            """
            SELECT id
            FROM urls
            WHERE short_code = %s;
            """,
            (short_code,)
        )

        existing_url = cursor.fetchone()

        if existing_url is None:
            return short_code

# Add a Root Endpoint
@app.get("/")
def home():
    return {
        "message": "URL Shortener API is running"
    }


# Create the POST /urls Endpoint

@app.post("/urls", status_code=status.HTTP_201_CREATED)
def create_short_url(url_data: URLCreate):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        short_code = generate_unique_short_code(cursor)

        cursor.execute(
            """
            INSERT INTO urls (
                short_code,
                original_url,
                user_id
            )
            VALUES (%s, %s, %s)
            RETURNING id, short_code, original_url, user_id, created_at;
            """,
            (
                short_code,
                str(url_data.original_url),
                1
            )
        )

        created_url = cursor.fetchone()

        connection.commit()

        return {
            "id": created_url[0],
            "short_code": created_url[1],
            "original_url": created_url[2],
            "user_id": created_url[3],
            "created_at": created_url[4]
        }

    except Exception:
        connection.rollback()
        raise

    finally:
        cursor.close()
        connection.close()


