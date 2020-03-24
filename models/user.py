import sqlite3


class UserModel:

    def __init__(self, id, username, password, sex, shoe_size, shirt_size, pant_size_waist, pant_size_length, shipping_address, billing_address):
        self.id = id
        self.username = username
        self.password = password
        self.sex = sex
        self.shoe_size = shoe_size
        self.pant_size_waist = pant_size_waist
        self.pant_size_length = pant_size_length
        self.shirt_size = shirt_size
        self.shipping_address = shipping_address
        self.billing_address = billing_address


    @classmethod
    def find_by_name(cls, name, db_path='./db/pineapplestore.db'):
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        query = 'SELECT * FROM user WHERE username=?;'
        result = cursor.execute(query, (name,))
        rows = result.fetchall()
        if rows:
            for row in rows:
                user = UserModel(row[0], row[1], row[2],row[3], row[4], row[5], row[6], row[7], row[8], row[9])
            connection.close()
            return user


    @classmethod
    def find_by_id(cls, id, db_path='./db/pineapplestore.db'):
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        query = 'SELECT * FROM user WHERE id=?'
        result = cursor.execute(query, (id,))
        rows = result.fetchall()
        if rows:
            for row in rows:
                user = UserModel(row[0], row[1], row[2],row[3], row[4], row[5], row[6], row[7], row[8], row[9])
            connection.close()
            return user

    @classmethod
    def insert_into_table(cls, username, password, db_path='./db/pineapplestore.db'):
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        query = 'INSERT INTO user VALUES(NULL, ?, ?,NULL,NULL,NULL,NULL,NULL,NULL)'
        cursor.execute(query, (username, password))
        connection.commit()
        connection.close()

    @classmethod
    def find_all(cls, db_path='./db/pineapplestore.db'):
        users = list()
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        query = 'SELECT * FROM user;'
        result = cursor.execute(query)
        rows = result.fetchall()
        if rows:
            for row in rows:
                users.append(UserModel(row[0], row[1], row[2],row[3], row[4], row[5], row[6], row[7], row[8], row[9]))
            return users
        connection.close()

    @classmethod
    def delete_user(self, name, db_path='./db/pineapplestore.db'):
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()

        user_id_query_for_purchase_his = 'SELECT id FROM user WHERE username=?;'
        user_id = cursor.execute(user_id_query_for_purchase_his, (name,))
        result_user_id = str(user_id.fetchone()[0])

        purchase_history_deletion = 'DELETE FROM purchase_history WHERE user_id=?;'
        delete_user_history = cursor.execute(purchase_history_deletion, (result_user_id))

        user_to_delete = 'DELETE FROM user WHERE username=?;'
        delete_user = cursor.execute(user_to_delete, (name,))
        connection.commit()
        connection.close()

    def json(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'sex': self.sex,
            'shoe_size': self.shoe_size,
            'shirt_size': self.shirt_size,
            'pant_size_waist': self.pant_size_waist,
            'pant_size_length': self.pant_size_length,
            'shipping_address': self.shipping_address,
            'billing_address': self.billing_address
            }

class AddressModel:

    def __init__(self, id, username, full_name, address1, address2, city, state, zipcode):
        self.id = id
        self.username = username
        self.full_name = full_name
        self.address1 = address1
        self.address2 = address2
        self.city = city
        self.state = state
        self.zipcode = zipcode

    @classmethod
    def get_default_billing(self, cls, city, db_path='./db/pineapplestore.db'):
        users = list()
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        query = 'SELECT * FROM billing_address;'
        result = cursor.execute(query)
        rows = result.fetchall()
        if rows:
            for row in rows:
                users.append(AddressModel(row[0], row[1], row[2],row[3], row[4], row[5], row[6], row[7]))
            return users
        connection.close()
    
    @classmethod
    def get_default_shipping(self, cls, city, db_path='./db/pineapplestore.db'):
        users = list()
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        query = 'SELECT * FROM shipping_address;'
        result = cursor.execute(query)
        rows = result.fetchall()
        if rows:
            for row in rows:
                users.append(AddressModel(row[0], row[1], row[2],row[3], row[4], row[5], row[6], row[7]))
            return users
        connection.close()

    def insert_into_table(self, cls, shipping_address, billing_address, db_path='./db/pineapplestore.db'):
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        query = 'INSERT INTO user VALUES(NULL, NULL, NULL, NULL,NULL,NULL,NULL,?,?)'
        cursor.execute(query, (shipping_address, billing_address))
        connection.commit()
        connection.close()

    def json(self):
        return {
            'id': self.id,
            'username': self.username,
            'full_name': self.full_name,
            'address1': self.address1,
            'address2': self.address2,
            'city': self.city,
            'state': self.state,
            'zipcode': self.zipcode 
        }