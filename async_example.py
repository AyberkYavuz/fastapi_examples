import asyncio
import requests
from fastapi import FastAPI

app = FastAPI()

urls = [
    "https://jsonplaceholder.typicode.com/posts",
    "https://jsonplaceholder.typicode.com/comments",
    "https://jsonplaceholder.typicode.com/albums",
    "https://jsonplaceholder.typicode.com/photos",
    "https://jsonplaceholder.typicode.com/todos",
    "https://jsonplaceholder.typicode.com/users"
]


async def fetch_data(url: str) -> dict:
    """Fetches data from the given URL and returns it as a JSON object.

    Args:
        url (str): The URL to fetch data from.

    Returns:
        dict: The JSON data returned by the URL.
    """
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


@app.get("/data")
async def get_data() -> list:
    """Fetches data from the URLs in parallel and returns the results as a list.

    Returns:
        list: A list of JSON data objects returned by the URLs.
    """
    tasks = [asyncio.create_task(fetch_data(url)) for url in urls]
    data = await asyncio.gather(*tasks)
    return data
