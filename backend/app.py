from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()

# Mount thư mục frontend để phục vụ file tĩnh
frontend_path = os.path.join(os.path.dirname(__file__), "../frontend")
app.mount("/frontend", StaticFiles(directory=frontend_path), name="frontend")

templates_path = os.path.join(os.path.dirname(__file__), "../frontend/templates")
templates = Jinja2Templates(directory=templates_path)


@app.get("/", response_class=HTMLResponse)
async def serve_index():
    with open(os.path.join(templates_path, "index.html"), "r") as f:

        return f.read()

# @app.get("/tool", response_class=HTMLResponse)
# async def serve_index():
#     with open(os.path.join(templates_path, "tool.html"), "r") as f:
#         return f.read()
    
@app.get("/contact", response_class=HTMLResponse)
async def serve_index():
    with open(os.path.join(templates_path, "contact.html"), "r") as f:
        return f.read()

@app.get("/tool", response_class=HTMLResponse)
async def tool(request: Request):
    return templates.TemplateResponse("tool.html", {"request": request, "show_nav": True, "show_sidebar": True})

@app.get("/tool1", response_class=HTMLResponse)
async def tool1(request: Request):
    return templates.TemplateResponse("tool1.html", {"request": request, "show_nav": True, "show_sidebar": True})

@app.get("/tool2", response_class=HTMLResponse)
async def tool2(request: Request):
    return templates.TemplateResponse("tool2.html", {"request": request, "show_nav": True, "show_sidebar": True})

@app.get("/tool3", response_class=HTMLResponse)
async def tool3(request: Request):
    return templates.TemplateResponse("tool3.html", {"request": request, "show_nav": True, "show_sidebar": True})


@app.get("/api/message")
def get_message():
    return {"message": "Hello from API"}

