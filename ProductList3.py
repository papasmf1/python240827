import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import uic 
import sqlite3
import os.path 

# 데이터베이스 처리 클래스
class DatabaseManager:
    def __init__(self, db_name):
        self.con = sqlite3.connect(db_name)
        self.cur = self.con.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS Products (id INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Price INTEGER);"
        )
        self.con.commit()

    def insert_product(self, name, price):
        self.cur.execute("INSERT INTO Products (Name, Price) VALUES (?, ?);", (name, price))
        self.con.commit()

    def update_product(self, prod_id, name, price):
        self.cur.execute("UPDATE Products SET Name=?, Price=? WHERE id=?;", (name, price, prod_id))
        self.con.commit()

    def delete_product(self, prod_id):
        self.cur.execute("DELETE FROM Products WHERE id=?;", (prod_id,))
        self.con.commit()

    def fetch_all_products(self):
        self.cur.execute("SELECT * FROM Products;")
        return self.cur.fetchall()

# UI 및 로직 처리 클래스
class Window(QMainWindow, uic.loadUiType("ProductList3.ui")[0]):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Database Manager 인스턴스 생성
        self.db = DatabaseManager("ProductList.db")

        # QTableWidget의 초기 설정
        self.setup_table()

        # 시그널 연결
        self.prodID.returnPressed.connect(lambda: self.focusNextChild())
        self.prodName.returnPressed.connect(lambda: self.focusNextChild())
        self.prodPrice.returnPressed.connect(lambda: self.focusNextChild())
        self.tableWidget.doubleClicked.connect(self.doubleClick)

        # 초기 데이터 로드
        self.getProduct()

    def setup_table(self):
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setHorizontalHeaderLabels(["제품ID", "제품명", "가격"])
        self.tableWidget.setTabKeyNavigation(False)

    def addProduct(self):
        name = self.prodName.text()
        price = self.prodPrice.text()
        self.db.insert_product(name, price)
        self.getProduct()

    def updateProduct(self):
        prod_id = self.prodID.text()
        name = self.prodName.text()
        price = self.prodPrice.text()
        self.db.update_product(prod_id, name, price)
        self.getProduct()

    def removeProduct(self):
        prod_id = self.prodID.text()
        self.db.delete_product(prod_id)
        self.getProduct()

    def getProduct(self):
        self.tableWidget.clearContents()
        products = self.db.fetch_all_products()
        for row, item in enumerate(products):
            # id 컬럼
            itemID = QTableWidgetItem(str(item[0]))
            itemID.setTextAlignment(Qt.AlignRight)
            self.tableWidget.setItem(row, 0, itemID)
            
            # 제품명 컬럼
            itemName = QTableWidgetItem(item[1])
            self.tableWidget.setItem(row, 1, itemName)
            
            # price 컬럼
            itemPrice = QTableWidgetItem(str(item[2]))
            itemPrice.setTextAlignment(Qt.AlignRight)
            self.tableWidget.setItem(row, 2, itemPrice)

    def doubleClick(self):
        self.prodID.setText(self.tableWidget.item(self.tableWidget.currentRow(), 0).text())
        self.prodName.setText(self.tableWidget.item(self.tableWidget.currentRow(), 1).text())
        self.prodPrice.setText(self.tableWidget.item(self.tableWidget.currentRow(), 2).text())

# 인스턴스를 생성하고 실행
app = QApplication(sys.argv)
myWindow = Window()
myWindow.show()
app.exec_()
