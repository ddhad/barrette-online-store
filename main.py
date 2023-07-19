import json
import sqlite3
import base64

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles


DB_NAME = "example.db"

templates = Jinja2Templates(directory="html")
app = FastAPI()

app.mount("/html", StaticFiles(directory="html"), name="html")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get("/product/{item_id}", response_class=HTMLResponse)
def get_product(item_id: int, request: Request):
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
        "price": item[2],
        "category": item[3],
        "series": item[4],
        "series_description": item[5],
        "brand": item[6],
        "quantity": item[7],
        "description": item[8],
        "usage": item[9],
        "ingredients": item[10],
        "images": json.dumps([
                base64.b64encode(img).decode('utf-8') for img in eval(item[11])
            ])
    }
    return templates.TemplateResponse(
        "product.html", {"request": request, "product": product}
    )


@app.get("/", response_class=HTMLResponse)
def get_home_page_(request: Request):
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
            "price": item[2],
            "category": item[3],
            "series": item[4],
            "series_description": item[5],
            "brand": item[6],
            "quantity": item[7],
            "description": item[8],
            "usage": item[9],
            "ingredients": item[10],
            "image": base64.b64encode(eval(item[11])[0]).decode('utf-8')
        }
        products.append(product)
    return templates.TemplateResponse(
        "helper.html", {"request": request, "products": json.dumps(products)}
    )
