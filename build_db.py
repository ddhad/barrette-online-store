import json
import sqlite3
import os

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price TEXT,
        category TEXT,
        series TEXT,
        series_description TEXT,
        brand TEXT,
        quantity REAL,
        description TEXT,
        usage TEXT,
        images BLOB
    )
''')

items_folder = 'example_items'
for item in os.listdir(items_folder):
    items = []
    for file in os.listdir(f'{items_folder}/{item}'):
        items.append(f'{item}/{file}')
    items.sort()

    row = {'images': [], 'data': None}
    for file in items:
        file = f'{items_folder}/{file}'
        if file.endswith('.json'):
            with open(file) as json_file:
                row['data'] = json.load(json_file)
        else:
            with open(file, 'rb') as image_file:
                row['images'].append(image_file.read())

    cursor.execute(
        "INSERT INTO items (name, price, category, series,"
        " series_description, brand, quantity, description,"
        " usage, images) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (row['data']['name'], row['data']['price'],
         row['data']['category'], row['data']['series'],
         row['data']['series_description'], row['data']['brand'],
         row['data']['quantity'], row['data']['description'],
         row['data']['usage'], repr(row['images']))
    )
conn.commit()
conn.close()
