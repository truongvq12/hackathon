import subprocess
import webbrowser
import os
import time

def run_backend():
    """Chạy backend FastAPI"""
    print("Starting backend...")
    try:
        subprocess.Popen(["uvicorn", "backend.app:app", "--reload"])
    except Exception as e:
        print(f"Error starting backend: {e}")

def run_frontend():
    """Mở frontend trong trình duyệt"""
    print("Opening frontend in browser...")
    time.sleep(2)  # Đợi backend khởi động
    webbrowser.open("http://localhost:8000/")

def main():
    """Chạy cả backend và frontend"""
    run_backend()
    run_frontend()

if __name__ == "__main__":
    main()
