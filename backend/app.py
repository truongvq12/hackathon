from fastapi.responses import HTMLResponse
import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Mount thư mục frontend để phục vụ file tĩnh
frontend_path = os.path.join(os.path.dirname(__file__), "../frontend")
app.mount("/frontend", StaticFiles(directory=frontend_path), name="frontend")

@app.get("/", response_class=HTMLResponse)
async def serve_index():
    with open(os.path.join(frontend_path, "index.html"), "r") as f:
        return f.read()

@app.get("/tool", response_class=HTMLResponse)
async def serve_index():
    with open(os.path.join(frontend_path, "tool.html"), "r") as f:
        return f.read()
    
@app.get("/contact", response_class=HTMLResponse)
async def serve_index():
    with open(os.path.join(frontend_path, "contact.html"), "r") as f:
        return f.read()



@app.get("/api/message")
def get_message():
    return {"message": "Hello from API"}

