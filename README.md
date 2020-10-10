# Stump map

Social project in scope of diploma for Learn Python.
The idea is to:

 - Track broken or forgotten trees and stumps in order to have fresh green tree instead
 - Allow communications between volunteer organizations and experts as well as cities administration
 - Track progress and help to create an order to the Administration

## Communication elements:
* Web interface
* Telegram Bot
	
## Integrations:
* Telegram [planned]
* Viber [under consideration]
* Facebook [under consideration]
* Twitter [under consideration]
* Email [under consideration]
* 
## Contribution:
 1. Make sure you understand the goal of the project and issues you'd like to solve
 2. Choose how would you like to help either development (front-, back-end) or UX or marketing or administrative support or anything else. 
 3. Find appropriate section in contribution 
 4. Have fun 

>Q: What to do if I want to contribute but don't see appropriate section?
A: Just drop us a line or create Pull Request 

### Volunteers:
[how volunteers can help]
### Administration:
[how administration can join and participate]
### Developers:
[where to find issue, ideas, roadmaps]

To run app locally:

Unix:
```
export FLASK_APP=webapp && export FLASK_ENV=development && flask run
```
Windows:
```
set FLASK_APP=webapp && set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run
```

### Set up local DB for development (using docker)

1. Install [Docker](https://docs.docker.com/get-docker/)
2. Run docker daemon on your machine
```
docker version
```
will show version instead of
```
error during connect:............
```
3. From docker\ folder run compose file
```
docker-compose up -d
```
it will start container with PostgresDB:
```
docker-compose up -d
CONTAINER ID        IMAGE       PORTS                    NAMES
b668d1df804c        postgres    0.0.0.0:5430->5432/tcp   docker_postgresql_1
```
>Port 5432 mapped to 5430


To initialize and migrate Database:
```python
python manage.py create_db
python manage.py db init
python manage.py db migrate
# to create test user
python manage.py create_user
```