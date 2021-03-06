import sqlite3
from models.user import UserModel


class PurchaseHistoryModel:

    db_path = './db/pineapplestore.db'

    def __init__(self, id, user_id, product_id):
        self.id = id
        self.user_id = user_id
        self.product_id = product_id

    @classmethod
    def find_history_product_by_userId(cls, userid):

        history_products = list()

        connection = sqlite3.connect(cls.db_path)
        cursor = connection.cursor()
        query = 'SELECT * FROM purchase_history WHERE user_id=?;'
        resluts = cursor.execute(query, (userid,))
        rows = resluts.fetchall()
        if rows:
            for row in rows:
                product = PurchaseHistoryModel(row[0], row[1], row[2])
                history_products.append(product)
            connection.close()
            return history_products

    @classmethod
    def find_products_related_with_user_name(cls, name):

        products_history_list = list()

        user = UserModel.find_by_name(name)
        if user:
            connection = sqlite3.connect(cls.db_path)
            cursor = connection.cursor()
            query = 'SELECT * FROM purchase_history WHERE user_id=?;'
            result = cursor.execute(query, (user.id,))
            rows = result.fetchall()
            if rows:
                for row in rows:
                    products = PurchaseHistoryModel(row[0], row[1], row[2])
                    products_history_list.append(products)
                connection.close()
                return products_history_list

    @classmethod
    def add_purchase(self, user_id, product_id):
        connection = sqlite3.connect('./db/pineapplestore.db')
        cursor = connection.cursor()
        query = 'INSERT INTO purchase_history VALUES(NULL, ?, ?);'
        cursor.execute(query, (user_id, product_id,))
        connection.commit()
        connection.close()

    def json(self):
        return {
            'purchase_id': self.id,
            'user_id': self.user_id,
            'product_id': self.product_id,
        }