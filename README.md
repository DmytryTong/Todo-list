# Todo-list

Django project for a website of a Todo-list application.


## Features

* Managing Tasks and tags.
* Powerful admin panel for advanced managing


## Instalation

pyton 3.11 must be already installed


## Project description
```
    Taks manager for a todo list of tasks, each task has its tags for a place, which connected with a task
```
## Database overlook:
```
     In this project models: Task, Tag were implemented.
 
     Tag has a "name" field, that describes name of a tag, 
 for example "Home", etc.
 
      Task has a "content" field, that describes task, "creation_date" creation 
 date for task, optional "deadline" field for task`s dealine, "complete" field 
 as indicator of complition of a task "tags" field - which contains tags, 
 attached for this task, as Many-to-Many field. 
```
# Demo:

 ![Todo-list - home_page.png](screenshots%2FTodo-list%20-%20home_page.png)
 ![Todo-list - tags_list.png](screenshots%2FTodo-list%20-%20tags_list.png)