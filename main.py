from typing import Union
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient
import urllib.parse


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

username = urllib.parse.quote_plus('Saurabh-0903')
password = urllib.parse.quote_plus('S@urabh0903')
conn = MongoClient("mongodb+srv://%s:%s@cluster0.caqfxk7.mongodb.net" % (username, password))


# @app.get("/", response_class=HTMLResponse)
# async def read_item(request: Request):
#     docs = conn.notes.notes.find({})
#     new_docs = []
#     for doc in docs:
#         new_docs.append({
#             "id": doc["_id"],
#             "note": doc["note"]
#         })
#     return templates.TemplateResponse("index.html", {"request": request, "new_docs": new_docs})


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}