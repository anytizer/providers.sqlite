import sqlite3
from provider import provider

user = ["a6@b.com", "pass1"]

conn = sqlite3.connect("cruder.db")

p = provider()
conn.create_function("GUID", 0, p.GUID)
conn.create_function("NOW", 0, p.NOW)
conn.create_function("SHA256", 1, p.SHA256)

cur = conn.cursor()
cur.execute("INSERT INTO users (user_id, user_email, user_password, created_on) VALUES (GUID(), ?, SHA256(?), NOW())", user)

conn.commit()
