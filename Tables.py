import sqlite3
conn = sqlite3.connect('shop.db')
c = conn.cursor()
c.execute('''CREATE TABLE users
             (id INTEGER PRIMARY KEY, username TEXT, password TEXT, role TEXT)''')
c.execute('''CREATE TABLE products
             (id INTEGER PRIMARY KEY, name TEXT, price REAL, quantity INTEGER)''')
c.execute('''CREATE TABLE orders
             (id INTEGER PRIMARY KEY, user_id INTEGER, product_id INTEGER, quantity INTEGER,
             FOREIGN KEY(user_id) REFERENCES users(id),
             FOREIGN KEY(product_id) REFERENCES products(id))''')
conn.commit()
conn.close()