# Add requirements.txt

PostgreSQL dependency <br>
```text
psycopg2-binary==2.9.12
python-dotenv
```

<br>

---

# .env

```text
import os
```

<br>
os is a built-in Python module. <br>
It gives Python access to things related to the operating system, including environment variables. <br>
<br>

```text
from dotenv import load_dotenv
```

<br>
This comes from the package: **python-dotenv**   which you already have in requirements.txt: <br>
python-dotenv <br>
Its job is to allow Python to read values from your .env file. <br>
<br>

```text
load_dotenv()
```

<br>
Find the .env file and load the variables from it so Python can access them. <br>


