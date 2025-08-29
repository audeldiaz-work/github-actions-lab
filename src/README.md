# fastapi-example

This project is a simple FastAPI application.

## Description

This application provides a basic API with two endpoints:

- A root endpoint that returns a "Hello World" message.
- An endpoint to retrieve items by their ID.

## Installation

To install the dependencies, run:

```bash
uv sync --locked
```

## Running the application

To run the application, use the following command:

```bash
uvicorn main:app --reload
```

## Endpoints

### Root

- **URL:** `/`
- **Method:** `GET`
- **Description:** Returns a simple "Hello World" greeting.
- **Example Response:**
  ```json
  {
    "Hello": "World"
  }
  ```

### Get Item by ID

- **URL:** `/items/{item_id}`
- **Method:** `GET`
- **Description:** Retrieves an item by its ID.
- **URL Parameters:**
  - `item_id` (integer, required): The ID of the item.
- **Query Parameters:**
  - `q` (string, optional): An optional query parameter.
- **Example Response:**
  ```json
  {
    "item_id": 123,
    "q": "some_query"
  }
  ```
