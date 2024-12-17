import subprocess
import webbrowser
import os
import time

def run_backend():
    """Chạy backend FastAPI"""
    print("Starting backend...")
    subprocess.Popen(["uvicorn", "backend.app:app", "--reload"])

def run_frontend():
    """Mở frontend trong trình duyệt"""
    print("Opening frontend in browser...")
    time.sleep(2)  # Đợi 2 giây để backend khởi động
    webbrowser.open("http://localhost:8000/")

def main():
    """Chạy cả backend và frontend"""
    run_backend()
    run_frontend()

if __name__ == "__main__":
    main()
