import sqlite3
import re
from typing import Pattern


# connection = sqlite3.connect('users_db.db')
# curs = connection.cursor()


def initiate_db():
    connection = sqlite3.connect('users_db.db')
    curs = connection.cursor()

    str_create_db = '''
    CREATE TABLE IF NOT EXISTS User(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    Age INT NOT NULL,
    balance INT NOT NULL)
    '''
    curs.execute(str_create_db)
    connection.commit()


# initiate_db()
# for i in range(1, 5):
#     curs.execute('INSERT INTO Products(username, email, Age, balance) VALUES(?, ?, ?, ?)',
#                   (f'Username{i}', f'Описание{i}', i * 100, list_img[i - 1]))


def get_all_products():
    connection = sqlite3.connect('users_db.db')
    curs = connection.cursor()
    curs.execute('SELECT * FROM Products')
    connection.commit()
    connection.close()
    return curs.execute('SELECT * FROM Products').fetchall()


def is_email(email: str) -> bool:
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, email):
        return True
    else:
        return False


def is_included(username):
    connection = sqlite3.connect('users_db.db')
    curs = connection.cursor()
    check_username = curs.execute('SELECT * FROM User WHERE username=?', (username,))
    return_check = False if check_username.fetchone() == None else True
    connection.close()
    return return_check


def add_user(username, email, age):
    connection = sqlite3.connect('users_db.db')
    curs = connection.cursor()
    if is_email(email):
        curs.execute('INSERT INTO User (username, email, Age, balance) VALUES(?, ?, ?, ?)',
                     (username, email, age, 1000))
    connection.commit()
    connection.close()


if __name__ == '__main__':
    # initiate_db()

    # print(is_included('Sergey'))
    add_user('Sergey', 'flot713@yandex.ru', 53)
    # add_user('Sergey', 'flot713@yandex.ru', 53)

a = 10
