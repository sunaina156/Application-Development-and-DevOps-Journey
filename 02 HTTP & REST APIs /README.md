# ***HTTP***

HTTP is a protocol(set of rules) which allows the fetching of resources, such as HTML(hyper text markup language) documents.

<img width="980" height="593" alt="image" src="https://github.com/user-attachments/assets/be3a3cbc-cac4-40e6-88b5-b579931711a5" />

The messages sent by the client usually a web browser are called requests and the messages sent by the server as an answer are called responses

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/f995b041-25bb-427e-9ff3-f0b402507712" />

HTTP clients (internet browsers) use TCP/IP or UDP networking protocol with HTTP to provide us the greatness and usefulness of WWW

<img width="1118" height="452" alt="image" src="https://github.com/user-attachments/assets/ba8f732f-f4a7-4fe6-9a1f-b80af70721bc" />

<img width="1920" height="1080" alt="Screenshot (1280)" src="https://github.com/user-attachments/assets/67370752-468d-4630-91ed-e5dc1236752f" />


## HTTP defines rules such as:

1. How to structure a request

Method → GET, POST, PUT, DELETE

URL/path → /index.html

Headers → Host, Content-Type, etc.

Body → data sent to the server, when needed

2. How the server should respond

HTTP/1.1 200 OK
Content-Type: text/html
<html>...</html>

HTTP defines what these mean:

200 → request was successful

404 → requested resource was not found

500 → server error

3. What different methods mean

GET → "Give me this data."

POST → "Here is some data; create/process it."

PUT → "Update/replace this resource."

DELETE → "Delete this resource."

## Definition
HTTP is a protocol that defines how a client and server format, send, receive, and understand messages over a network.

---
---

# ***HTTP Request***

A request is sent by the client to the server.


for ex:
GET /products

A request contains important information such as:
Method, URL, Headers, Body (sometimes)


Example:
POST /api/urls
Content-Type: application/json
{
  "long_url": "https://example.com"
} 

---

