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

### extracting_parameter_values.py

Just have a look at [extracting_parameter_values.py](https://github.com/AyberkYavuz/fastapi_examples/blob/main/extracting_parameter_values.py)

In this example, we define a POST endpoint that accepts a request body with a JSON object containing an Item model. 
The Item model is defined using Pydantic's BaseModel, which allows us to define the expected structure of the JSON object.

When you make a POST request to this endpoint with a valid JSON object, FastAPI will automatically parse the request 
body and validate it against the Item model. 
If the JSON object is valid, FastAPI will pass an instance of the Item model to the create_item function.

to run it, use this command in your terminal

```bash
uvicorn extracting_parameter_values:app --reload
```

Here's an example of a valid JSON object that you could use to test **/items/** endpoint:

```json
{
    "name": "Foo",
    "price": 50.2,
    "is_offer": true
}
```

### fastapi_ml_server.py

Just have a look at [fastapi_ml_server.py](https://github.com/AyberkYavuz/fastapi_examples/blob/main/fastapi_ml_server.py)

This file is the heart of ml engineering.

Please read the docstrings of the methods.

the post method makes the server handle the concurrent requests!

to run it, use this command in your terminal

```bash
uvicorn fastapi_ml_server:app --reload 
```

Here's an example of a valid JSON object that you could use to test **/predict_class** endpoint:

```json
{
  "sepal_length": 5.1, 
  "sepal_width": 3.5, 
  "petal_length": 1.4, 
  "petal_width": 0.2
}
```

## FaskAPI vs Flask 

| Server Type | Number of Users | Average Response Time (Milliseconds) | Error % | Throughput |
|-------------|-----------------|--------------------------------------|---------|------------|
| Flask       | 150             | 481                                  | 0.0     | 105.2/sec  |
| Flask       | 200             | 836                                  | 0.0     | 111.2/sec  |
| Flask       | 250             | 1124                                 | 0.0     | 117.2/sec  |
| Flask       | 300             | 1421                                 | 5.0     | 119.3/sec  |
| Flask       | 350             | 1472                                 | 5.43    | 125.8/sec  |
| Flask       | 400             | 1603                                 | 10.25   | 132.8/sec  |


