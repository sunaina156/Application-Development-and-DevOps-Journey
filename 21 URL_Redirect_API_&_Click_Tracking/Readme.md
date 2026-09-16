# What is a Redirect?

A redirect tells the browser to visit another URL. <br>

For example: <br>

```text
User requests:
http://localhost:8000/abc123

Application finds:
https://github.com

Application responds:
"Go to https://github.com"
```

# Where are redirects used in other applications?

```text
After login → redirect to dashboard
After logout → redirect to login page
Payment success → redirect to success page
OAuth authentication → redirect to callback URL
URL shorteners → redirect to the original URL
```

So, redirecting is a general web development concept, not specific to URL Shorteners. <br>

---

# Learn a Simple Redirect Example

redirect_example.py <br>

```text
from fastapi import FastAPI
from fastapi.responses import RedirectResponse


app = FastAPI()


@app.get("/go-to-github")
def go_to_github():
    return RedirectResponse(
        url="https://github.com",
        status_code=307
    )
```

Run: <br>
uvicorn redirect_example:app --reload <br><br>

Open: <br>

http://localhost:8000/go-to-github
 <br>
Your browser will redirect to GitHub. <br>
<br>

So: <br>
RedirectResponse(url="https://github.com") <br>

This returns a redirect response instead of normal JSON. <br>

---

# Learn Database-Based Redirects

In a real application, we usually don't hardcode the destination. <br>

Instead, we retrieve it from the database. <br>

**General logic** <br>

```text
        Receive an identifier
short_code, product_id, order_id, etc.
                  ⬇ 
        Search the database
                  ⬇
      Check whether the record exists
                  ⬇
           Perform an action
Redirect, display, update, or create data
````

This pattern can be used in many backend applications. <br>

---

# Learn Click Tracking

Click tracking means recording an event whenever a user performs an action. <br>

For example: <br>

```text
A user clicks a short URL.
A user opens a product.
A user views a post.
A user downloads a file.
```

 <br>

We can record: <br>

```text
Who performed the action?
What was accessed?
When did it happen?
```

 <br> <br>
For your URL Shortener: <br>

```text
Field            Meaning
url_id         Which URL was opened
ip_address     Visitor's IP address
clicked_at     Time of the click
```

Your clicks table already supports this. <br>

---

```text
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import RedirectResponse

from db import get_connection


app = FastAPI()


@app.get("/redirect/{short_code}")
def redirect_example(
    short_code: str,
    request: Request
):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        # 1. Find the URL
        cursor.execute(
            """
            SELECT id, original_url
            FROM urls
            WHERE short_code = %s;
            """,
            (short_code,)
        )

        result = cursor.fetchone()

        # 2. Check if the URL exists
        if result is None:
            raise HTTPException(
                status_code=404,
                detail="Short URL not found"
            )

        url_id = result[0]
        original_url = result[1]

        # 3. Get visitor IP address
        visitor_ip = None

        if request.client is not None:
            visitor_ip = request.client.host

        # 4. Record the click
        cursor.execute(
            """
            INSERT INTO clicks (
                url_id,
                ip_address
            )
            VALUES (%s, %s);
            """,
            (url_id, visitor_ip)
        )

        # 5. Save the click
        connection.commit()

        # 6. Redirect the user
        return RedirectResponse(
            url=original_url,
            status_code=307
        )

    except HTTPException:
        connection.rollback()
        raise

    except Exception:
        connection.rollback()
        raise

    finally:
        cursor.close()
        connection.close()
```

<br>

---

















