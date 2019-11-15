# fastapi
Python REST APIs with FastAPI

## Get Started

1. Install the required packages and dependencies

  ```bash
  $ pip install -r requirements.txt
  ```

2. Run the API server

    ```bash
    $ uvicorn app.main:app --reload
    ```

3. Hit the API

    * http://localhost:8000/items/5?q=somequery
   
4. View the docs

    * http://localhost:8000/docs
    
    or
    
    * http://localhost:8000/redoc

## What does it use?

* FastAPI
* Uvicorn - webserver
* Pydantic - type checking, schema and model definition, etc.
