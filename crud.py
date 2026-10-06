from fastapi import FastAPI
from routers.productRouter import studentRouter


app = FastAPI(
    title="FastAPI Student CRUD"
)


app.include_router(studentRouter)


@app.get("/")
def home():
    return {
        "message": "FastAPI Student CRUD API is running"
    }
