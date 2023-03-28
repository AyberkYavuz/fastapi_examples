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