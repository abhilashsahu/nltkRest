# TestProject

## Running with docker

```
git clone git@github.com:abhilashsahu/nltkRest.git

docker-compose up

# If the server is running successfully at http://0.0.0.0:8000/ consider the rest app is up
To Extract the URL use following details/example

REQUEST
    URL: http://0.0.0.0:8000
    Endpoint: /app/v1/keywords/
    Request type: POST
    Content-Type: application/json
    Request body: {"text": "This is a text data and keyword extraction"}

RESPONSE
    Status: HTTP 200 OK
    Data: {
    "keywords": [
        "text data",
        "keyword extraction"
    ]
}

```

### Developed and Tested using below backend tools, technologies, frameworks or modules:
```
    OS: macOS Ventura 13.4.1
    IDE: PyCharm 2023.1.4 (Professional Edition)
    Python: 3.10
    django: 4.2.3
    DB: Sqlite3
    djangorestframework: 3.14.0
```
