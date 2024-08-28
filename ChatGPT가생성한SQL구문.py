import sqlite3
import random

class ElectronicsDatabase:
    def __init__(self, db_name="electronics.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS products (
            product_id INTEGER PRIMARY KEY,
            product_name TEXT NOT NULL,
            price REAL NOT NULL
        )
        '''
        self.conn.execute(query)
        self.conn.commit()

    def insert_product(self, product_id, product_name, price):
        query = '''
        INSERT INTO products (product_id, product_name, price)
        VALUES (?, ?, ?)
        '''
        self.conn.execute(query, (product_id, product_name, price))
        self.conn.commit()

    def update_product(self, product_id, product_name=None, price=None):
        query = "UPDATE products SET "
        params = []
        
        if product_name is not None:
            query += "product_name = ?, "
            params.append(product_name)
        
        if price is not None:
            query += "price = ?, "
            params.append(price)
        
        query = query.rstrip(', ') + " WHERE product_id = ?"
        params.append(product_id)
        
        self.conn.execute(query, tuple(params))
        self.conn.commit()

    def delete_product(self, product_id):
        query = '''
        DELETE FROM products WHERE product_id = ?
        '''
        self.conn.execute(query, (product_id,))
        self.conn.commit()

    def select_products(self):
        query = '''
        SELECT * FROM products
        '''
        cursor = self.conn.execute(query)
        return cursor.fetchall()

    def close(self):
        self.conn.close()

# 메인 코드

# 데이터베이스 클래스 초기화
db = ElectronicsDatabase()

# 샘플 데이터 생성
product_names = [f"Product_{i}" for i in range(1, 101)]
prices = [round(random.uniform(10.0, 1000.0), 2) for _ in range(100)]

# 데이터베이스에 샘플 데이터 삽입
for i in range(100):
    db.insert_product(i + 1, product_names[i], prices[i])

# 데이터 확인 (앞의 10개 제품 출력)
products = db.select_products()
for product in products[:10]:
    print(product)

# 데이터베이스 연결 종료
db.close()
