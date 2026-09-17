# What Is Software Testing?

Testing means checking whether your application behaves as expected. <br>

For example, your URL Shortener should: <br>

- Create a short URL for valid input.

- Reject invalid URLs.

- Return 404 for a missing short code.

- Reject unauthenticated requests.

- Return a JWT after successful login.

- Record clicks when a short URL is accessed.

 <br> <br>
Without testing, you might manually check each feature after every code change. <br> <br>

With automated testing: <br>

```text
Developer changes code
        |
        v
Automated tests execute
        |
        v
Tests pass or fail
        |
        v
Application can continue through CI/CD
```

<br>

---

# Types of Testing

## Unit Testing

Tests one small part of your application in isolation. <br>

Example: <br>

```text
def add_numbers(a, b):
    return a + b
```

 <br>
Test: <br>

```text
assert add_numbers(2, 3) == 5
```

 <br> <br>
Unit tests are generally: <br>
- Fast
- Focused
- Easy to debug

 <br> <br>

 ## Integration Testing

Checks whether multiple components work together. <br>

Example: <br>

```text
FastAPI endpoint
       |
       v
Database connection
       |
       v
PostgreSQL query
```

 <br>
For your project, a test might verify that creating a URL correctly inserts data into PostgreSQL. <br> <br>

## End-to-End Testing

Tests a complete user workflow. <br>

Example: <br>

```text
Register user
     |
     v
Login
     |
     v
Receive JWT
     |
     v
Create short URL
     |
     v
Open short URL
     |
     v
Record click
```

 <br> <br>

 ## Regression Testing

Checks that existing functionality has not broken after a change. <br>

Example: <br>

You add authentication, then verify that URL redirection still works. <br> <br>

---

# Testing Pyramid

A common testing strategy is: <br>

Testing Pyramid <br>

```text

                                        ----E2E----    

                              -------------Integration------------  

         ---------------------------------Unit Tests------------------------------  
```
Generally, many unit tests, fewer integration tests, and a smaller number of end-to-end tests. <br>

This is a guideline, not a strict rule. The right balance depends on your application. <br>

---

# Install Pytest

Activate your virtual environment: <br>

```text
cd C:\Users\sunaina\Desktop\Python_URL_Shortener\Python_URL_Shortener 

.\venv\Scripts\Activate.ps1
```

 <br>
Install testing dependencies: <br>

```text
pip install pytest httpx
```

 <br>
Update your requirements file: <br>

```text
pip freeze > requirements.txt
```

 <br>
FastAPI's TestClient uses HTTPX and Starlette's testing functionality.
 <br>

 ---

 # Create a Test Directory

Create the following structure: <br>

```text
Python_URL_Shortener/
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── db.py
│   ├── models.py
│   ├── security.py
│   ├── dependencies.py
│   └── routes/
│       ├── auth.py
│       └── urls.py
│
├── tests/
│   ├── __init__.py
│   ├── test_main.py
│   ├── test_security.py
│   └── test_urls.py
│
├── database.sql
├── seed.sql
├── requirements.txt
├── .env
└── pytest.ini
```

<br>
The tests/ directory contains your automated tests.
<br>

---

# Understand Assertions

An assertion checks whether a condition is true. <br>

```text
assert 2 + 3 == 5
```

<br>
This passes. <br> <br>

```text
assert 2 + 3 == 6
```

<br>
This fails. <br> <br>

Common assertions <br>

```text
assert result == expected
assert result is not None
assert "message" in response.json()
assert response.status_code == 200
```

<br>
If an assertion fails, Pytest reports the failure. <br>

---

# Your First Unit Test

Create: <br>

tests/test_security.py <br>

Add: <br>

```text
from app.security import (
    hash_password,
    verify_password
)


def test_password_hash_is_different_from_plain_password():
    password = "TestPassword123"

    hashed_password = hash_password(password)

    assert hashed_password != password


def test_password_verification_succeeds():
    password = "TestPassword123"

    hashed_password = hash_password(password)

    assert verify_password(
        password,
        hashed_password
    ) is True


def test_password_verification_fails_for_wrong_password():
    password = "TestPassword123"

    hashed_password = hash_password(password)

    assert verify_password(
        "WrongPassword",
        hashed_password
    ) is False
```

 <br>
What are we testing? <br>

```text
Password hash should not equal the original password.
Correct password should be accepted.
Incorrect password should be rejected.
```

 <br> <br>
Run: <br>

```text
pytest tests/test_security.py -v
```

Expected result: <br>

```text
3 passed
```

 <br>
You must run the command yourself to confirm the actual result.

<br>

---

# Test JWT Functions

Add the following tests to tests/test_security.py: <br>

```text
import pytest

from app.security import (
    create_access_token,
    decode_access_token
)


def test_access_token_contains_user_id():
    user_id = 1

    token = create_access_token(user_id)

    decoded_user_id = decode_access_token(token)

    assert decoded_user_id == user_id


def test_invalid_token_is_rejected():
    invalid_token = "invalid.jwt.token"

    with pytest.raises(ValueError):
        decode_access_token(invalid_token)
Explanation
with pytest.raises(ValueError):
```

<br>
means: <br>

The test expects this code to raise a ValueError. <br>
 
If no exception is raised, the test fails. <br>

---

# FastAPI TestClient

FastAPI provides a test client for sending requests to your application without manually starting Uvicorn. <br>

Create: <br>

tests/test_main.py <br>

Add: <br>


```text
from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_home_endpoint():
    response = client.get("/")

    assert response.status_code == 200

    assert response.json() == {
        "message": "URL Shortener API is running"
    }
```

<br> <br>
Run: <br>

```text
pytest tests/test_main.py -v
```

<br> <br>

Important <br>

This test imports your FastAPI application directly: <br>

```text
from app.main import app
```

<br>
You do not need to run: <br>

```text
uvicorn app.main:app --reload
```

<br>
in another terminal for this test. <br>


<br> <br>

```text
if we are not running application as a package

> $env:PYTHONPATH = ".\app"
tells test_main.py to find main.py in app folder

Test the import
> python -c "from main import app; print('Import successful')"


Run your test
If you see Import successful, run:
> pytest tests/test_main.py -v
```

<br>

---

# Testing HTTP Status Codes

HTTP status codes are important in API testing <br>

```text
Status         Meaning
200         Successful request
201         Resource created
307         Temporary redirect
400          Bad request
401          Authentication required or failed
404         Resource not found
409         Conflict
422         Validation error
500         Internal Server error
```

<br>

Example: <br>

```text
def test_missing_route_returns_404():
    response = client.get("/route-that-does-not-exist")

    assert response.status_code == 404
```

<br>

---

# Testing Validation

Your URLCreate model uses: <br>

```text
class URLCreate(BaseModel):
    original_url: HttpUrl
```

 <br>
FastAPI should reject invalid URLs. <br> <br>

Add to tests/test_urls.py: <br>

```text
from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_invalid_url_is_rejected():
    response = client.post(
        "/urls",
        json={
            "original_url": "not-a-valid-url"
        }
    )

    assert response.status_code == 422
```

 <br> <br>
**Important authentication consideration** <br>

Because your /urls endpoint is protected, the request might return 401 before validation is processed, depending on FastAPI's dependency and validation behavior.
 <br>
Therefore, do not assume this test will always return 422 without checking your actual endpoint behavior. <br> <br>

A more reliable test for the Pydantic model alone is: <br>

```text
import pytest
from pydantic import ValidationError

from app.models import URLCreate


def test_invalid_url_model():
    with pytest.raises(ValidationError):
        URLCreate(
            original_url="not-a-valid-url"
        )

```

 <br>

 ---

 # Testing Protected Endpoints

Your URL creation endpoint requires authentication: <br>

```text
current_user_id: int = Depends(
    get_current_user_id
)
```

 <br>
Therefore, a request without a token should be rejected. <br> <br>

Add to tests/test_urls.py: <br>

```text
def test_create_url_without_token_is_rejected():
    response = client.post(
        "/urls",
        json={
            "original_url": "https://github.com"
        }
    )

    assert response.status_code == 401
```

 <br>
Run: <br>

```text
pytest tests/test_urls.py -v
```

 <br> <br> <br>
Why test authentication? <br>

Because a security change should be verified. <br>
 <br>
You need to ensure: <br>

```text
Anonymous users cannot create URLs.
Valid tokens are accepted.
Invalid tokens are rejected.
The correct user ID is used.
```

 <br>

 ---

 # Mocking: Why Is It Needed?

Testing your actual database during every unit test can be: <br>

```text
Slow
Difficult to configure
Dependent on database state
Risky if tests modify real data
Mocking replaces a real dependency with a controlled test object.
```

 <br>
Example: <br>

```text
Actual database connection
          |
          v
      Replaced by
          |
          v
    Mock database
```

 <br>
You can test application behavior without connecting to PostgreSQL. <br>

---

# Simple Mocking Example

Create: <br>
tests/test_example.py <br>

```text
from unittest.mock import Mock


def get_greeting(user_service):
    return user_service.get_name()


def test_get_greeting():
    mock_service = Mock()

    mock_service.get_name.return_value = "Sunaina"

    result = get_greeting(mock_service)

    assert result == "Sunaina"

    mock_service.get_name.assert_called_once()
```

 <br> <br>
Explanation <br>

```text
mock_service = Mock()
```

 <br>
Creates a mock object. <br>

mock_service.get_name.return_value = "Sunaina" <br>

Defines what the mocked method should return. <br>

assert_called_once() <br>

Checks that the method was called exactly once. <br>

---

# Testing URL Creation Without a Real Database

Your current route directly calls: <br>

```text
get_connection()
```

 <br>
To unit-test it properly, you can mock the database connection. <br>

However, your endpoint includes database cursor behavior, transaction handling, and unique short-code generation. A complete mock must reproduce the methods your route calls. <br> <br>

A simplified example: <br>

```text
from unittest.mock import Mock


def test_mock_database_cursor():
    mock_connection = Mock()
    mock_cursor = Mock()

    mock_connection.cursor.return_value = mock_cursor

    mock_cursor.fetchone.return_value = (
        "abc123",
    )

    cursor = mock_connection.cursor()

    result = cursor.fetchone()

    assert result == ("abc123",)

    mock_connection.cursor.assert_called_once()
    mock_cursor.fetchone.assert_called_once()
```

 <br>
This tests mock behavior, not your actual SQL correctness. <br>

For database integration tests, use a separate test database rather than relying exclusively on mocks. <br>

---

# Important: Do Not Use Your Production Database for Tests

Your application currently uses: <br>

```text
DB_NAME=url_shortener
```

 <br>
Avoid running destructive tests against your normal practice database. <br> <br>

Create a separate test database: <br>

```text
CREATE DATABASE url_shortener_test;
```

 <br>
A proper test setup can use: <br>

```text
TEST_DB_NAME=url_shortener_test
```

 <br> <br>
For a more advanced project, you could use: <br>

```text
A dedicated PostgreSQL test database.
Docker Compose for PostgreSQL.
Temporary database schemas.
Database transactions that are rolled back after each test.
Test fixtures.
```

 <br>
Do not add these complexities until your basic tests are working.
 <br>
 
---

 # Pytest Configuration

Create: <br>

pytest.ini <br>

Add: <br>

```text
[pytest]
testpaths = tests
python_files = test_*.py
python_functions = test_*
```

 <br>
Now you can run all tests from the project root: <br>

```text
pytest -v
```

 <br>
You can also run: <br>

```text
python -m pytest -v
```

 <br>
The second command explicitly runs Pytest through your active Python interpreter. <br>

---

# Useful Pytest Commands

```text
Run all tests
pytest -v

Run one file
pytest tests/test_security.py -v

Run one test
pytest tests/test_security.py::test_password_verification_succeeds -v

Show print statements
pytest -v -s

Stop after the first failure
pytest -x

Run tests matching a keyword
pytest -k password -v
```

<br>
Show test coverage <br>

Install:

```text
pip install pytest-cov
```

<br>
Run: <br>

```text
pytest --cov=app -v
```

<br>
Coverage indicates which parts of your code were executed by tests. High coverage does not automatically mean high-quality tests.
<br>

---

# Test Fixtures

Fixtures provide reusable test setup. <br>

Example: <br>

```text
import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def api_client():
    return TestClient(app)
```

 <br> <br>
Use it: <br>

```text
def test_home_endpoint(api_client):
    response = api_client.get("/")

    assert response.status_code == 200
```

 <br> <br>
Why fixtures are useful <br> <br>

Without a fixture: <br>

client = TestClient(app) <br>

might be repeated across multiple files. <br> <br>

With fixtures, common setup can be reused. <br> <br> <br>

Later, you can create fixtures for: <br>

```text
Database connections
Test users
Authentication tokens
Mock services
Temporary files
```


---

# Testing Strategy for Your Project

Start with these tests: <br>

```text
Phase 1: Unit tests

Password hashing
Password verification
JWT creation
JWT decoding
Invalid JWT rejection
Pydantic model validation
```

<br>

```text
Phase 2: API tests

Home endpoint
Registration
Login
Unauthorized URL creation
URL creation with valid authentication
Redirect for existing short code
404 for missing short code
```

<br>

```text
Phase 3: Integration tests

URL is inserted into PostgreSQL.
Click record is inserted.
User ID comes from the authenticated token.
Transaction rollback works after database errors.
```

<br>

---

# Testing and CI/CD

A DevOps pipeline may follow this structure: <br>

```text
Git push
   |
   v
Install dependencies
   |
   v
Run linting
   |
   v
Run automated tests
   |
   v
Build Docker image
   |
   v
Deploy application
```

<br>


If tests fail: <br>

```text
Tests failed
     |
     v
Pipeline stops
     |
     v
Developer investigates
```

<br>
This prevents many defective changes from reaching deployment 
<br>

---
















