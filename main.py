from fastapi import FastAPI

from routers.ai_summary_router import router as ai_summary_router


app = FastAPI(
    title="AI Summary API"
)


app.include_router(
    ai_summary_router
)


@app.get("/")
async def root():
    return {
        "message": "AI Summary API is running"
    }