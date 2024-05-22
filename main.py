from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to my first api!"}


@app.get("/posts")
def get_posts():
    return {"data": "This is a list of posts"}


@app.post("/post/create")
def create_post(payload: dict = Body(...)):
    print(payload)
    return {"New_post": f"Post created with title: {payload['title']} and body: {payload['content']}"}
