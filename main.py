import sqlite3
import base64

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware


DB_NAME = "example.db"

templates = Jinja2Templates(directory="html")
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get("/item/{item_id}", response_class=HTMLResponse)
def get_item(item_id: int, request: Request):
    con = sqlite3.connect(DB_NAME, check_same_thread=False)
    cur = con.cursor()
    cur.execute(f"""SELECT * FROM items WHERE id = {item_id}""")
    item = cur.fetchone()
    cur.close()
    con.close()

    if not item:
        return {'ERROR': 'PRODUCT NOT FOUND'}
    product = {
        "id": item[0],
        "name": item[1],
        "description": item[2],
        "price": item[3],
        "category": item[4],
        "image": base64.b64encode(item[5]).decode("utf-8")
    }
    return templates.TemplateResponse(
        "product.html", {"request": request, "product": product}
    )


@app.get("/items/")
def get_all_items():
    con = sqlite3.connect(DB_NAME, check_same_thread=False)
    cur = con.cursor()
    cur.execute("""SELECT * FROM items""")
    items = cur.fetchall()
    cur.close()
    con.close()

    products = []
    for item in items:
        product = {
            "id": item[0],
            "name": item[1],
            "description": item[2],
            "price": item[3],
            "category": item[4],
            "image": base64.b64encode(item[5]).decode("utf-8")
        }
        products.append(product)

    return products
