# fastapi_examples
This repository is for containing source codes of examples of fastapi.

## Installation
```bash
pip3 install fastapi 

pip3 install uvicorn 
```

## Description

### hello_fastapi.py
Just have a look at [hello_fastapi.py](https://github.com/AyberkYavuz/fastapi_examples/blob/main/hello_fastapi.py)

to run it, use this command in your terminal

```bash
uvicorn main:app --reload
```

### custom_router.py

You can write a custom router to route urls to class methods.

Just have a look at [custom_router.py](https://github.com/AyberkYavuz/fastapi_examples/blob/main/custom_router.py)

to run it, use this command in your terminal

```bash
uvicorn custom_router:app --reload
```

After that use postman to create requests and get responses from get and post methods of the class.

### async/await

async/await is a powerful feature in Python that allows you to write asynchronous code that can run concurrently. 
FastAPI is built on top of Starlette, which itself is built on top of the ASGI specification. 
This makes it very easy to write asynchronous code in FastAPI.

async makes your tasks running at the same time by calling the function that includes the logic 
(long running operations like db select, network operations, etc).

By using await you can send your response after all tasks are finished

### async_example.py

Just have a look at [async_example.py](https://github.com/AyberkYavuz/fastapi_examples/blob/main/async_example.py)

Read the docstrings of the functions.

to run it, use this command in your terminal

```bash
uvicorn async_example:app --reload
```

After that trigger **/data** url