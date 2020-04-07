import sqlite3
from provider import provider

user = ["a6@b.com", "pass1"]

connection = sqlite3.connect("cruder.db")

p = provider()
connection.create_function("GUID", 0, p.GUID)
connection.create_function("NOW", 0, p.NOW)
connection.create_function("SHA256", 1, p.SHA256)
connection.create_function("CONCAT_WS", -1, p.CONCAT_WS)

insert_sql = """
INSERT INTO users (
    user_id, user_email, user_password, created_on, user_notes
) VALUES (
    GUID(), ?, SHA256(?), NOW(), CONCAT_WS('-', 'a', 'b', 'c')
);"""
cursor = connection.cursor()
cursor.execute(insert_sql, user)

connection.commit()
connection.close()
