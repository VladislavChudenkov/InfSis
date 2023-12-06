import sqlite3
class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.c = self.conn.cursor()
    def add_user(self, user):
        self.c.execute("INSERT INTO users VALUES (?, ?, ?, ?)",
                       (user.id, user.username, user.password, user.role))
        self.conn.commit()
    def add_product(self, product):
        self.c.execute("INSERT INTO products VALUES (?, ?, ?, ?)",
                       (product.id, product.name, product.price, product.quantity))
        self.conn.commit()
    def add_order(self, order):
        self.c.execute("INSERT INTO orders VALUES (?, ?, ?, ?)",
                       (order.id, order.user_id, order.product_id, order.quantity))
        self.conn.commit()
    def get_users(self):
        self.c.execute("SELECT * FROM users")
        return self.c.fetchall()
    def get_products(self):
        self.c.execute("SELECT * FROM products")
        return self.c.fetchall()
    def get_orders(self):
        self.c.execute("SELECT * FROM orders")
        return self.c.fetchall()
    def close(self):
        self.conn.close()

