from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import time
import asyncio

app = FastAPI()

@app.middleware("http")
async def request_time(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    duration = time.time() - start
    response.headers["Request-Process-Time"] = f"{duration}"
    return response

#------SYNC ENDPOINT------
@app.get("/sync-task")
def sync_task():
    time.sleep(5) #blocking
    return {"message": "Sync task completed after 5 seconds"}

#------ASYNC ENDPOINT-----
@app.get("/async-task")
async def task():
    await asyncio.sleep(5)  # Non-blocking async sleep
    return {"message": "task completed after 5 seconds"}