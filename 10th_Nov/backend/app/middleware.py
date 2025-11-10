import logging
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

logger = logging.getLogger("middleware")
logging.basicConfig(level=logging.INFO)

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        logger.info(f"Request: {request.method} {request.url}")
        try:
            response = await call_next(request)
            logger.info(f"Response: {response.status_code}")
            return response
        except Exception as e:
            logger.error(f"Unhandled error: {e}", exc_info=True)
            return Response(content=f"Internal Server Error: {e}", status_code=500)
