from fastapi import FastAPI
import requests
import json

API_KEY = "AIzaSyCxlO5qac9RsUfe-1Iit6O7aSY8WAqZqBA"

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, Uvicorn and FastAPI!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)