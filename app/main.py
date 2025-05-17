from fastapi import FastAPI, Request, Body

from typing import Optional
from .logger import logger
from .tasks import process_data

app = FastAPI()

@app.post("/process")
async def process_input(
    data: Optional[str] = Body(default="", media_type="text/plain"),
    request: Request = None
):
    """
    API endpoint to receive raw text data, log the input, and trigger background processing.

    This endpoint accepts plain text in the body (not JSON), logs the client's IP and the input,
    then enqueues a Celery task (`process_data`) to process the input asynchronously.

    Args:
        data (Optional[str]): Raw input text sent in the request body as plain text. Defaults to empty string.
        request (Request, optional): FastAPI request object used to extract client IP. Defaults to None.

    Returns:
        dict: A JSON response containing a message and the ID of the submitted background task.
    """
    client = request.client.host if request else "unknown"
    logger.info(f"[INPUT] From {client}: {repr(data)}")

    # Submit task to Celery
    task = process_data.delay(data or "")
    logger.info(f"[TASK] Submitted task ID: {task.id} for input: {repr(data)}")

    return {"message": "Task submitted", "task_id": task.id}
