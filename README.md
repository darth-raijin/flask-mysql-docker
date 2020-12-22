# 🐋 Template | Get started with Flask, MySQL and Docker!

A simple ready-to-go template, to get started with above mentioned tech. This template is easily customizeable, where changes are easy to make.
I tried to emphasise where the changes should be made, but generally background knowledge with Docker, Flask and MySQL is recommended.

## Technologies
Project is created with:
* Python version: 3.8.5
* MySQL version: 5.7
* Docker version: 3.5
	
## Setup
To run this project, clone the repository. 
Open a terminal on the folder, followed by:

```
$ docker-compose up --build
```

To get into the MySQL container:
```
$ docker exec -it <container_name> bash
```

## How to modify

### Database
To connect in database.py, it is important to first set a name for the database in the init.sql file.
```SQL
CREATE DATABASE __change;
```

The chosen name must also be used for the following variable in database.py:
```python
self.__db = "__change"
```
