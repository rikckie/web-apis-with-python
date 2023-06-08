from typing import List
from typing import Optional
from fastapi import FastAPI
from fastapi import Query 
from fastapi.encoders import jsonable_encoder
from model.dbHandler import match_exact
from model.dbHandler import match_like

app = FastAPI()


@app.get("/")
def index():
    """
    DEFAULT ROUTE
    This method will
    1. Provide usage instructions formatted as JSON
    """
    return jsonable_encoder({"usage":"/dict?=<word>"})


@app.get("/dict")
def dictionary(word:str):
    """
    DEFAULT ROUTE
    This method will
    1. Accept a word from the request
    2. Try to find an exact match, and return it if found
    3. If not found, find all approximate matches and return
    """
    # 1. Accept a word from the request
    if not word:
        return jsonable_encoder({"status":"error",
                                "word":word,
                                "data":"word not found"})
    definitions = match_exact(word)
    if definitions:
        return jsonable_encoder({"stats":"success",
                                 "word":word,
                                 "data":definitions})
    definitions = match_like(word)
    if definitions:
        return jsonable_encoder({"stats":"partial",
                                 "word":word,
                                 "data":definitions})
    else:
        return jsonable_encoder({"status":"error",
                                "word":word,
                                    "data":"word not found"})

