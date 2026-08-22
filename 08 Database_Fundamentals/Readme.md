# Database

Organized collection of data that allows applicatons to store, retrieve, modify, and manage information efficiently. <br>
Ex: Imagine your URL shortener  have URLS, and store them in json but json won't work for 10 millon URLS, 1 million users, millions of requests per day, multiple application servers etc. <br>

**A database gives mechanism for:** <br>
- efficient searching
- Updating data
- Deleting data
- Handling many users
- Maintaining data consistency
- Managing relationships
- Controlling access
- Handling concurrent operations
- Recovering from failures

---

# Why we need Databases?
Suppose we have a application for company. <br>
It needs to store: <br>

```text
Users
Products
Orders
Payments
URLs
Comments
Messages
Logs
```

We need more than just a place to put data. <br>
We need to answer questions such as: <br>

```text
Find this user
Find all orders belonging to this user
Delete this product
Find all orders from today
Find the most popular URLs
Make sure two users don't get the same username
```

A database provides tools to perform these operations efficiently and reliably.

---


