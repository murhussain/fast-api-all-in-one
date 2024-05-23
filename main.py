from typing import Optional

from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = False
    rating: Optional[int] = None


my_post = [
    {"id": 1, "title": "Post 1", "content": "This is the content of post 1", "published": True, "rating": 5},
    {"id": 2, "title": "Post 2", "content": "This is the content of post 2", "published": False, "rating": 4},
    {"id": 3, "title": "Post 3", "content": "This is the content of post 3", "published": True, "rating": 3},
    {"id": 4, "title": "Post 4", "content": "This is the content of post 4", "published": False, "rating": 2},
    {"id": 5, "title": "Post 5", "content": "This is the content of post 5", "published": True, "rating": 4},
]


@app.get("/")
async def root():
    return {"message": "Welcome to my first api!"}


@app.get("/posts")
def get_posts():
    return {"data": my_post}


@app.post("/posts")
def create_post(post: Post):
    post_dict = post.dict()
    post_dict["id"] = randrange(0, 1000000)
    my_post.append(post_dict)
    return {"data": {
        "message": "Post created successfully",
        "data": post_dict
    }}
