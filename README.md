# Python API Testing with Requests Module

This README provides guidance on testing REST APIs using the `requests` module in Python. 

## Prerequisites

Before getting started, ensure you have the following libraries installed:

1. `requests`: You can install it via pip:
    ```
    pip install requests
    ```
2. `jsonpath`: You can install it via pip:
    ```
    pip install jsonpath
    ```

## Understanding the API

To understand how to perform GET, POST, PUT, and DELETE requests, visit [reqres.in](https://reqres.in/). This site provides a mock REST API that you can interact with for testing purposes. Additionally, you can use [JSON Viewer](https://jsonviewer.stack.hu/) to visualize JSON data in a table format, which can assist in writing code to retrieve data.

### CRUD Operations

- **Create (POST):** Use POST requests to create new resources.
- **Read (GET):** Use GET requests to retrieve existing resources.
- **Update (PUT/PATCH):** Use PUT or PATCH requests to update existing resources.
- **Delete (DELETE):** Use DELETE requests to remove existing resources.

#### PUT vs PATCH

- **PUT:** Updates or replaces the entire resource with the provided data. If the record exists, it updates; otherwise, it creates a new one.
- **PATCH:** Updates or modifies specific properties of the resource. It doesn't require sending the entire object, only the properties to be updated.

### Timeout Handling

Handle slow API responses effectively by setting timeouts. For example, if a payment process should complete within 30 seconds, configure a timeout to ensure the request doesn't hang indefinitely.

### Basic Authentication

Some APIs may require basic authentication. You can test this functionality on [the-internet.herokuapp.com](https://the-internet.herokuapp.com/).

## Example Usage

Here's a basic example of using `requests` for API testing:

```python
import requests

# Example GET request
response = requests.get('https://reqres.in/api/users/1')
print(response.json())

# Example POST request
data = {
    "name": "John",
    "job": "Engineer"
}
response = requests.post('https://reqres.in/api/users', json=data)
print(response.json())

# Example PUT request
data = {
    "name": "Jane",
    "job": "Developer"
}
response = requests.put('https://reqres.in/api/users/2', json=data)
print(response.json())

# Example PATCH request
data = {
    "job": "Manager"
}
response = requests.patch('https://reqres.in/api/users/2', json=data)
print(response.json())

# Example DELETE request
response = requests.delete('https://reqres.in/api/users/2')
print(response.status_code)
