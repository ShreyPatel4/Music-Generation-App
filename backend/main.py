
from fastapi import FastAPI
from routers import music_router, prompt_router
import uvicorn

app = FastAPI(title="Music Generation App", version="1.0.0")

app.include_router(music_router.router)
app.include_router(prompt_router.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
