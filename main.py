import controllers
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/auth/spotify-callback")
def spotify_callback_get(code: Union[str,None]):
    print(code)
    return {"success": True}


@app.get("/auth/spotify-login")
def spotify_login():
    print("login")
    response = controllers.redirect_to_spotify()
    return response
