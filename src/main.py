"""
This module defines a simple FastAPI application.
It includes endpoints for retrieving a greeting and items by ID.
"""
from typing import Union


from fastapi import FastAPI
from datetime import datetime

app = FastAPI()


@app.get("/timestamp")
def get_timestamp() -> dict:
    """
    Endpoint that returns the current server timestamp in ISO format.

    Returns:
        dict: A dictionary containing the server timestamp.
    """
    from datetime import timezone
    return {"timestamp": datetime.now(timezone.utc).isoformat()}


@app.get("/")
def read_root() -> dict:
    """
    Root endpoint that returns a greeting.

    Returns:
        dict: A dictionary containing a greeting message.
    """
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None) -> dict:
    """
    Endpoint to retrieve an item by its ID.

    Args:
        item_id (int): The ID of the item to retrieve.
        q (Union[str, None], optional): An optional query parameter.
            Defaults to None.
    Returns:
        dict: A dictionary containing the item ID and the query parameter
            (if provided).
    """
    return {"item_id": item_id, "q": q}
