# TestProject

## Running with docker

```
git clone git@github.com:abhilashsahu/nltkRest.git

[//]: # (docker-compose run web python3.10 manage.py createcachetable)

[//]: # ()
[//]: # (docker-compose run web python3.10 manage.py migrate #migrate django db inside container)

docker-compose up

# If the server is running successfully at http://0.0.0.0:8000/ consider the backned is up
Check the URL: [http://0.0.0.0:8000/app/v1/keywords/](http://0.0.0.0:8000/app/v1/keywords/)

```

### Developed and Tested using below backend tools, technologies, frameworks or modules:
```
    OS: macOS Monterey 12.0.1
    IDE: PyCharm 2021.2.1 (Community Edition)
    Python: 3.10
    django: 4.1.7
    DB: Sqlite3
    djangorestframework: 3.14.0
```

