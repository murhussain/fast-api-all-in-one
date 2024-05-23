from typing import Optional

from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = False
    rating: Optional[int] = None


@app.get("/")
async def root():
    return {"message": "Welcome to my first api!"}


@app.get("/posts")
def get_posts():
    return {"data": "This is a list of posts"}


@app.post("/post/create")
def create_post(post: Post):
    print(post)
    print(post.dict())
    return {"data": post}
