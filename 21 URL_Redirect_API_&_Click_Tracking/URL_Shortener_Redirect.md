Continuation of: <br>
https://github.com/sunaina156/Application-Development-and-DevOps-Journey/tree/main/20%20URL_Shortener_With_FastAPI


---

Update app_main.py

```text
from fastapi import FastAPI, status
```

replace it with: <br>

```text
from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import RedirectResponse
```

<br>

```text
HTTPException -> Return errors such as 404 Not Found
Request -> Access request information, such as IP address
RedirectResponse -> Redirect the browser to another URL
```

## Add the redirect endpoint

Go to the bottom of your existing api_main.py file, after your create_short_url() function. <br>

```text
@app.get("/{short_code}")
def redirect_to_original_url(
    short_code: str,
    request: Request
):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        # 1. Find the original URL using the short code
        cursor.execute(
            """
            SELECT id, original_url
            FROM urls
            WHERE short_code = %s;
            """,
            (short_code,)
        )

        result = cursor.fetchone()

        # 2. Return 404 if the short code does not exist
        if result is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Short URL not found"
            )

        url_id = result[0]
        original_url = result[1]

        # 3. Get the visitor's IP address
        visitor_ip = None

        if request.client is not None:
            visitor_ip = request.client.host

        # 4. Insert a click record
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

        # 5. Commit the click record
        connection.commit()

        # 6. Redirect to the original URL
        return RedirectResponse(
            url=original_url,
            status_code=status.HTTP_307_TEMPORARY_REDIRECT
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


## Test Your Updated Application

**Start FastAPI** <br>

```text
uvicorn api_main:app --reload
```

**Create a short URL** <br>

Open: <br>

```text
http://localhost:8000/docs
```

Use POST /urls:  <br>

```text
{
  "original_url": "https://github.com"
}
```

 <br>
Copy the generated short code. <br>

**Open the short URL**

In your browser: <br>

```text
http://localhost:8000/YOUR_SHORT_CODE
```

Expected result: <br>

Browser opens GitHub. <br>

Click is recorded in PostgreSQL. <br>

**Verify the click**  <br>

In PostgreSQL: <br>

```text
\c url_shortener
```

```text
SELECT
    id,
    url_id,
    ip_address,
    clicked_at
FROM clicks
ORDER BY id DESC;
```


Check the original URL connected to each click: <br>

```text
SELECT
    clicks.id AS click_id,
    urls.short_code,
    urls.original_url,
    clicks.ip_address,
    clicks.clicked_at
FROM clicks
JOIN urls
    ON clicks.url_id = urls.id
ORDER BY clicks.id DESC;
```



