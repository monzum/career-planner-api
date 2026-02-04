"""
Logging middleware for FastAPI.

This middleware runs for every HTTP request.
It logs:

- HTTP method (GET/POST/etc.)
- Request path
- Unique request ID
- Response status code
- Time taken to process the request
- Date + timestamp (UTC)

When deployed to AWS, these logs will go to CloudWatch automatically.
"""

import time
import uuid
from datetime import datetime

from fastapi import Request


async def logging_middleware(request: Request, call_next):
    """
    Middleware function that logs details about every incoming request.

    Args:
        request (Request): Incoming HTTP request object.
        call_next (Callable): Function that forwards the request to the next
                              middleware or the route handler.

    Returns:
        Response: The HTTP response returned by the endpoint.
    """

    # Generate a unique ID for this request (helps trace logs in distributed systems)
    request_id = str(uuid.uuid4())

    # Record the start time so we can calculate duration later
    start_time = time.time()

    # Call the actual endpoint / next middleware in the chain
    response = await call_next(request)

    # Calculate how long the request took (in seconds)
    duration = time.time() - start_time

    # Current timestamp in UTC ISO format (e.g., 2026-02-04T10:23:11Z)
    timestamp = datetime.utcnow().isoformat() + "Z"

    # Print structured log line (stdout is captured by AWS / Docker logs)
    print(
        f"{timestamp} | "
        f"{request.method} {request.url.path} | "
        f"request_id={request_id} | "
        f"status={response.status_code} | "
        f"duration={duration:.3f}s"
    )

    return response
