import sqlite3
from provider import provider

user = ["a6@b.com", "pass1"]

conn = sqlite3.connect("cruder.db")

p = provider()
conn.create_function("GUID", 0, p.GUID)
conn.create_function("NOW", 0, p.NOW)
conn.create_function("SHA256", 1, p.SHA256)
conn.create_function("CONCAT_WS", -1, p.CONCAT_WS)

cur = conn.cursor()
insert_sql = """
INSERT INTO users (
    user_id, user_email, user_password, created_on, user_notes
) VALUES (
    GUID(), ?, SHA256(?), NOW(), CONCAT_WS('-', 'a', 'b', 'c')
);"""
cur.execute(insert_sql, user)

conn.commit()
