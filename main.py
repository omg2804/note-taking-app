from fastapi import FastAPI
from routers import note_router

app = FastAPI()

app.include_router(note_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Note Taking App!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)