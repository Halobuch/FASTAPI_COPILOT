import base64
import os
from typing import Any
from pathlib import Path
from hashlib import sha256

from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from products import router as products_router

app = FastAPI()
app.include_router(products_router)
STATIC_DIR = Path(__file__).parent / "static"


class GenerateRequest(BaseModel):
    prompt: str


# Create a Pydantic model named Text with one required string field, text.
class Text(BaseModel):
    text: str


@app.get("/")
async def index() -> FileResponse:
    return FileResponse(STATIC_DIR / "index.html")


@app.post("/generate")
async def generate(request: GenerateRequest) -> dict[str, str]:
    return {"result": f"Received prompt: {request.prompt}"}


# Create a FastAPI endpoint that accepts a POST request with a JSON body containing a single field called "text" and returns a checksum of the text
@app.post("/checksum")
async def checksum(request: Text) -> dict[str, str]:
    digest = sha256(request.text.encode("utf-8")).hexdigest()
    return {"checksum": digest}


@app.post("/payload")
async def receive_payload(payload: dict[str, Any]) -> dict[str, Any]:
    return {"received": payload}