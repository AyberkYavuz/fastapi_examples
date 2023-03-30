# fastapi_examples
This repository is for containing source codes of examples of fastapi.

## Required Packages Installation
```bash
pip3 install -r requirements.txt
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

### flask_ml_server.py

Just have a look at [flask_ml_server.py](https://github.com/AyberkYavuz/fastapi_examples/blob/main/flask_ml_server.py)

This file is the flask implementation of fastapi_ml_server.py.

I want to compare the performances of flask and fastapi ml servers.

to run flask_ml_server.py, click the run button of your code editor. 

## Load Testing

Load testing of machine learning backend APIs has several benefits, including:

1. Scalability testing: Load testing helps to assess the scalability of the machine learning backend API. By simulating high traffic scenarios, you can determine how well the API can handle a large number of requests and users.

2. Performance optimization: Load testing can also help to identify bottlenecks and performance issues in the machine learning backend API. This can enable developers to optimize the code and infrastructure to improve the API's performance.

3. Stability testing: Load testing can reveal any stability issues in the machine learning backend API. By simulating different scenarios and load levels, you can identify potential failure points and areas that need improvement.

4. Cost optimization: Load testing can help to optimize costs associated with the machine learning backend API. By identifying the maximum load that the API can handle, developers can determine the optimal infrastructure configuration needed to support the expected traffic and usage levels.

5. Increased user satisfaction: By identifying and addressing performance issues through load testing, machine learning backend APIs can provide a better user experience. This can lead to increased user satisfaction and retention.

In summary, load testing of machine learning backend APIs is crucial for assessing scalability, identifying performance bottlenecks and stability issues, optimizing costs, and providing a better user experience.

## FastAPI vs Flask 

I used **Apache JMeter** to collect some KPIs of ml backend APIs.

**Note:** These tests were done on my local machine.

**My Local Machine Information:**

- MacBook Pro (15-inch, 2018)
- Processor: 2,2 GHz 6-Core Intel Core i7
- Memory: 16 GB 2400 MHz DDR4

### Load Test Results Table's Columns Descriptions

**Server Type:** The type of server which is flask or fastapi.

**Number of Users:** The number of users is the total number of virtual users or clients that interact with the system or application during a load test. This metric is crucial because it helps determine the maximum capacity of the system to handle a certain number of users simultaneously.

**Average Response Time (Milliseconds):** The average response time is the average time it takes for the system or application to respond to a user's request. It is usually measured in milliseconds. A high response time can indicate performance issues and can negatively impact user experience.

**Error %:** The error percentage represents the percentage of requests that the system or application fails to handle successfully. It is a measure of the system's ability to handle unexpected errors and exceptions. A high error percentage can indicate performance issues or bugs in the system.

**Throughput:** Throughput refers to the rate at which the system or application can process requests during a load test. It is usually measured in requests per second. A high throughput indicates that the system can handle a high volume of requests without performance degradation or errors.

### Load Test Results Table

| Server Type | Number of Users | Average Response Time (Milliseconds) | Error % | Throughput |
|-------------|-----------------|--------------------------------------|---------|------------|
| Flask       | 150             | 481                                  | 0.0     | 105.2/sec  |
| FastAPI     | 150             | 183                                  | 0.0     | 124.9/sec  |
| Flask       | 200             | 836                                  | 0.0     | 111.2/sec  |
| FastAPI     | 200             | 405                                  | 0.0     | 133.6/sec  |
| Flask       | 250             | 1124                                 | 0.0     | 117.2/sec  |
| FastAPI     | 250             | 479                                  | 0.0     | 154.9/sec  |
| Flask       | 300             | 1421                                 | 5.0     | 119.3/sec  |
| FastAPI     | 300             | 915                                  | 0.0     | 146.8/sec  |
| Flask       | 350             | 1472                                 | 5.43    | 125.8/sec  |
| FastAPI     | 350             | 952                                  | 0.0     | 152.9/sec  |
| Flask       | 400             | 1603                                 | 10.25   | 132.8/sec  |
| FastAPI     | 400             | 1034                                 | 0.0     | 157.6/sec  |
| Flask       | 450             | 1642                                 | 18.67   | 144.8/sec  |
| FastAPI     | 450             | 1247                                 | 0.0     | 165.3/sec  |
| Flask       | 500             | 1674                                 | 21.40   | 154.8/sec  |
| FastAPI     | 500             | 1366                                 | 0.40    | 171.8/sec  |


As you can see, FastAPI performs better on all user groups.
