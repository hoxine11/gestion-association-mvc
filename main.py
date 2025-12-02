from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from views.api import app as api_app
import os


app = FastAPI(
    title="Association Management System",
    description="MVC Architecture with Repository Pattern and Observer Pattern",
    version="1.0.0"
)


# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Mount API routes
app.mount("/api", api_app)


# Serve static files (if you have CSS/JS folder)
if os.path.exists("views/web/static"):
    app.mount("/static", StaticFiles(directory="views/web/static"), name="static")


@app.get("/")
async def read_root():
    """Serve the main web interface"""
    return FileResponse("views/web/index.html")


@app.get("/dashboard.html")
async def read_dashboard():
    """Serve the dashboard page"""
    return FileResponse("views/web/dashboard.html")


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "ok",
        "message": "Association Management System is running",
        "patterns": ["Repository Pattern", "Observer Pattern"]
    }


if __name__ == "__main__":
    import uvicorn
    print("="*60)
    print("🕌 نظام إدارة الجمعية القرآنية")
    print("="*60)
    print("📋 Architecture: MVC")
    print("🔧 Patterns: Repository + Observer")
    print("🌐 Server: http://127.0.0.1:8000")
    print("📊 Dashboard: http://127.0.0.1:8000/dashboard.html")
    print("📚 API Docs: http://127.0.0.1:8000/api/docs")
    print("="*60)
    uvicorn.run(app, host="127.0.0.1", port=8000)
