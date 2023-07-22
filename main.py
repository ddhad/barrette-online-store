import json
import sqlite3
import base64
import random

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles


DB_NAME = "db/barrette.db"

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

    if not item:
        return {'ERROR': 'PRODUCT NOT FOUND'}

    series = item[5]
    cur.execute(
        f"SELECT * FROM items WHERE series = '{series}' AND id != {item_id}"
    )
    related_items = cur.fetchall()
    random.shuffle(related_items)

    cur.close()
    con.close()

    related_products = []
    for r_item in related_items[0:4]:
        r_image = eval(r_item[14])
        if len(r_image) > 0:
            r_image = base64.b64encode(r_image[0]).decode('utf-8')
        else:
            r_image = None
        related_product = {
            "id": r_item[0],
            "bg_name": r_item[2],
            "image": r_image
        }
        related_products.append(related_product)

    product = {
        "id": item[0],
        "barcode": item[1],
        "bg_name": item[2],
        "en_name": item[3],
        "material_code": item[4],
        "series": item[5],
        "series_description": item[6],
        "product_type": item[7],
        "short_description": item[8],
        "description": item[9],
        "usage": item[10],
        "ingredients": item[11],
        "benefits": item[12],
        "size": item[13],
        "images": json.dumps([
                base64.b64encode(img).decode('utf-8') for img in eval(item[14])
            ])
    }
    return templates.TemplateResponse(
        "product.html", {
            "request": request,
            "product": product,
            "related_products": related_products
        }
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
    for item in items[0:8]:
        image = eval(item[14])
        if len(image) > 0:
            image = base64.b64encode(image[0]).decode('utf-8')
        else:
            image = None
        product = {
            "id": item[0],
            "barcode": item[1],
            "bg_name": item[2],
            "en_name": item[3],
            "material_code": item[4],
            "series": item[5],
            "series_description": item[6],
            "product_type": item[7],
            "short_description": item[8],
            "description": item[9],
            "usage": item[10],
            "ingredients": item[11],
            "benefits": item[12],
            "size": item[13],
            "image": image
        }
        products.append(product)
    return templates.TemplateResponse(
        "helper.html", {"request": request, "products": json.dumps(products)}
    )
