# Shopping REST API

## Project Description
This project was inspired by an assignment from one of my courses at STU FEI University in the subject *Object-Oriented Programming (OOP)*.  
I reworked the assignment into Python and added some extra logic to a few endpoints.

## Setup Instructions

### Install FastAPI and Uvicorn
```bash
pip install fastapi uvicorn
````

### Start the Server

```bash
uvicorn main:app --reload
```

Explanation of the command:

* `main` → the filename (`main.py`)
* `app` → the FastAPI instance (`app = FastAPI()`)
* `--reload` → automatically restarts the server when you change the code

## Explore the REST API

Open one of the following in your browser:

* API root: 👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* Interactive docs (Swagger UI): 👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* Alternative docs (ReDoc): 👉 [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
