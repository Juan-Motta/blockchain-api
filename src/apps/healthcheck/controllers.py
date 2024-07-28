from fastapi.requests import Request
from .schemas import HealthCheckResponse


async def healthcheck(request: Request):
    """
    Handles a health check request to verify if the service is running.

    This function responds with a simple health check message indicating the service status.

    Args:
        request (Request): The request object.

    Returns:
        HealthCheckResponse: A response object containing a health check message.
    """
    return HealthCheckResponse(message="ok")
