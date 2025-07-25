## Flask TODO API  
A beginner-friendly RESTful TODO API built with Python Flask using simple in-memory Python lists. This API allows you to create, read, update, and delete todo items as long as the app is running.

### 📦 Features
* Simple and lightweight

* No database or external dependencies

* In-memory storage (resets every time app restarts)

* REST-API routes

### 🚀 Getting Started 

#### 🔧 Requirements

* Python 3.x
* pip

### 📥 Installation
Clone this repository or create a new Python file (app.py):

>git clone https://github.com/rsdecoder/todo-project.git

<code>cd flask-todo-inmemory</code>

#### Install Flask:
>pip install flask 
> 
### ▶️ Run the App
>python app.py


### 📚 API Endpoints


| Method | Endpoint    | Description         |
|--------|-------------|---------------------|
| GET    | /todos      | Get all todos       |
| POST	  | /todos      | Create a new todo   |
| GET    | /todos/:id	 | Get a specific todo |
| PUT    | /todos/:id	 | Update a todo       |
| DELETE | /todos/:id	 | Delete a todo       |


You can test the API using insomnia or postman or by using curl commands

>### ⚠️ Note
>Data is not saved between restarts because it uses a Python list, not a database.

