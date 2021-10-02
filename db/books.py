import sqlite3
from sqlite3 import Error
from .connection import create_connection

def insert_book(data):
    conn = create_connection()
    sql = """ INSERT INTO books (title, category, page_qty, book_path, description)
                VALUES(?, ?, ?, ?, ?)
    """

    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("Nuevo Libro Agregado")
        return True
    except Error as e:
        print("Error insertando el libro" + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()


def update_book(__id,data):
    conn = create_connection()
    sql = f""" UPDATE books SET
                            title = ?,
                            category = ?,
                            page_qty = ?,
                            page_qty_read = ?,
                            book_path = ?,
                            desription = ?
                where book_id = {__id}
    """
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print("Libro Actualizado")
        return True
    except Error as e:
        print("Error al actualizar el libro" + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def delete_book(__id):
    conn = create_connection()
    sql = f"DELETE FROM books WHERE book_id = {__id}"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print("Libro Eliminado")
        return True
    except Error as e:
        print("Error al eleminar el libro" + str(e))
    finally:
        cur.close()
        conn.close()

def select_all_books():
    conn = create_connection()
    sql = "SELECT * FROM books"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        return books
    except Error as e:
        print("Error al obtener libros" + str(e))
    finally:
        cur.close()
        conn.close()

def select_book_by_id(__id):
    conn = create_connection()
    sql = f"SELECT * FROM books WHERE book_id = {__id}"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        book = cur.fetchone()
        return book
    except Error as e:
        print("Error al buscar el libro" + str(e))
    finally:
        cur.close()
        conn.close()

def select_book_by_title(title):
    conn = create_connection()
    sql = f"SELECT * FROM books WHERE title LIKE '%{title}%'"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        return books
    except Error as e:
        print("Error al buscar el libro" + str(e))
    finally:
        cur.close()
        conn.close()

def select_book_by_category(category):
    conn = create_connection()
    sql = f"SELECT * FROM books WHERE title LIKE '%{category}%'"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        return books
    except Error as e:
        print("Error al buscar el libro" + str(e))
    finally:
        cur.close()
        conn.close()