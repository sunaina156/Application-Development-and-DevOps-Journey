# ***HTTP***

HTTP is a protocol(set of rules) which allows the fetching of resources, such as HTML(hyper text markup language) documents.

<img width="980" height="593" alt="image" src="https://github.com/user-attachments/assets/be3a3cbc-cac4-40e6-88b5-b579931711a5" />

The messages sent by the client usually a web browser are called requests and the messages sent by the server as an answer are called responses

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/f995b041-25bb-427e-9ff3-f0b402507712" />

HTTP clients (internet browsers) use TCP/IP or UDP networking protocol with HTTP to provide us the greatness and usefulness of WWW

<img width="1118" height="452" alt="image" src="https://github.com/user-attachments/assets/ba8f732f-f4a7-4fe6-9a1f-b80af70721bc" />

<img width="1920" height="1080" alt="Screenshot (1280)" src="https://github.com/user-attachments/assets/67370752-468d-4630-91ed-e5dc1236752f" />


**HTTP defines rules such as:**

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

**HTTP is a protocol that defines how a client and server format, send, receive, and understand messages over a network.**

---
---

# ***HTTP Request***

**A request is sent by the client to the server.**

for ex:   <br>
GET /products  

**A request contains important information such as:** <br>
Method, URL, Headers, Body (sometimes)  

**Example:**  <br>
POST /api/urls  <br>
Content-Type: application/json    <br>
{                            <br>
  "long_url": "https://example.com"    <br>
}                       <br>

---
# HTTP Response

**The server sends a response back to the client**

**For ex:**   <br>
HTTP/1.1 201 Created   <br>
{    <br>
  "short_url": "https://short.ly/aB92x"   <br>
}    <br>

**A response usually contains:**   <br>
Status Code  <br>
Headers   <br>
Body (sometimes)

---
# HTTP Methods

<img width="940" height="527" alt="image" src="https://github.com/user-attachments/assets/763f0517-a32b-407a-a47f-b5cb3f797550" />

HTTP methods tell the server what the client wants to do.   <br>

**The most important ones are:**   <br>
GET        ->    Retrieve data         <br>
POST      ->    Create data         <br>
PUT        ->    Replace/update data         <br>
PATCH    ->    Partially update data         <br>
DELETE  ->    Delete data         <br>

**Example**   <br>
/api/urls           <br>

We might have:   <br> 
GET         /api/urls/    <br> 
POST       /api/urls    <br> 
GET         /api/urls/123   <br> 
DELETE   /api/urls/123    <br> 

## GET
GET is generally used to retrieve data   <br>

Ex:      <br>
GET /api/urls     <br>
means: Give me the URLS    <br>

Ex:   <br>
GET /api/urls/123   <br>
means: Give m URL number 123 <br>

## POST
POST is generally used to create something or submit data.   <br>

For URL Shortener:   <br>
POST /api/urls/   <br>

Request:    <br>
{   <br>
   "long_url": "https://example.com"   <br>
}   <br>

Backend might respond:   <br>
{   <br>
   "short_url": "https://short.ly/aB92x"   <br>
}   <br>

## **PUT vs PATCH**    <br>
These are both for updates    <br>

### PUT    <br>
Usually means replace the resource    <br>

### PATCH    <br>
Usually means partially update the resource    <br>

For ex:    <br>
**PUT /users/10**    <br>
could replace the users's complete information    <br>

While:    <br>
**PATCH /users/10**    <br>
could change only:    <br>
{    <br>
  "name": "Sunaina"    <br>
}    <br>

## DELETE    <br>
Used to delete something    <br>

Ex:    <br>
**DELETE /api/urls/123**    <br>
Means:    <br>
Delete url 123.    <br>

---
# HTTP Status Codes

<img width="980" height="609" alt="image" src="https://github.com/user-attachments/assets/4fbd6ed4-cd3d-4316-8811-1ec60750e152" />

The server uses status codes to tell the client what happened.

**2xx - Success**  <br>
200    OK  <br>
201    Created  <br>
204    No Content  <br>

**3xx - Redirection**  <br>
301   Moved Permanently  <br>
302   Found / Temporary Redirect  <br>

**4xx - Client Error**  <br>
400    Bad Request  <br>
401    Unauthorized  <br>
403    Forbidden  <br>
404    Not Found  <br>

**5xx - Server Error**  <br>
500    Internal Server Error  <br>
502    Bad Gateway  <br>
503    Service Unavailable  <br>


## Important Status Codes

**200   OK**
Request succeeded  <br>

GET /users  <br>
-> 200   OK  <br>

**201   Created**
Something was successfully created  <br>

POST /api/urls  <br>
-> 201  Created  <br>

This is perfect for URL shortener when a short URL is created  <br>

**400  Bad Request**
The client send invalid data  <br>

Ex:  <br>
{  <br>
    "long_url": "hello"  <br>
}  <br>

when a valid URL was required  <br>

**401   Unauthorized**
The user needs to authenticate  <br>

**403 Forbidden**
The server understood the request but refuses to allow it  <br>

**404  Not Found**
The request resource doesn't exist  <br>

ex:  <br>
GET /api/urls/99999  <br>
-> 404 Not Found  <br>

**500 Internal Server Error**
Something went wrong on the server  <br>

---
# JSON


---
What are HTTP headers<br>

metadata -> key-value sent along with request and response<br>

caching, authentication, manage state <br>
x- prfix  -> 2012 (X- deprecated)

Request Headers            -> from Client         <br> 
Response Headers          -> from server          <br>
Representation Headers -> encoding / compression  <br>
Payload Headers             -> data              <br>
                               (id, email etc)   <br>

**Most common Headers**
- Accept : application/josn
- User-Agent
- Authorization
- Content-Type
- Cookie
- Cache-Control

**CORS**
- Access-Control-Allow-Origin
- Access-Control-Allow-Credentials
- Access-Control-Allow-Method

**Security**
- Cross-Origin-Embedder-Policy
- Cross-Origin-Opener-Policy
- Content-Security-Policy
- X-XSS-Protection

---

