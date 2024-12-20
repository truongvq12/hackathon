from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os
from fastapi import FastAPI, Request, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import os
from dotenv import load_dotenv
from pydantic import BaseModel
import openai

app = FastAPI()

env_path = os.path.join(os.path.dirname(__file__), "../.env")
load_dotenv(dotenv_path=env_path)
openai_api_key = os.getenv("OPENAI_API_KEY")

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


class ChatRequest(BaseModel):
    message: str

from fastapi import HTTPException
from pydantic import BaseModel
import openai

class ChatRequest(BaseModel):
    message: str

@app.post("/api/chat")
async def chat_with_gpt(chat_request: ChatRequest):
    print(f"OpenAI API Key: {openai_api_key}")  # Kiểm tra API key
    if not openai_api_key:
        raise HTTPException(status_code=500, detail="API key không được tìm thấy hoặc không hợp lệ")

    # Thiết lập API key cho OpenAI
    openai.api_key = openai_api_key

    try:
        # Gửi yêu cầu tới GPT API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": chat_request.message}]
        )
        # Trả về kết quả
        reply = response["choices"][0]["message"]["content"]
        return {"reply": reply}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"OpenAI Error: {str(e)}")

