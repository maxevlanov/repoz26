import sqlite3

conn = sqlite3.connect("db.db")
cur = conn.cursor()


cur.execute("""
CREATE TABLE IF NOT EXISTS categories(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER,
    is_published BOOLEAN DEFAULT (false),
    name_en TEXT NOT NULL,
    name TEXT NOT NULL,
    FOREIGN KEY (parent_id) REFERENCES categories(id)
);
""")
conn.commit()
cur.execute("""
CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id INTEGER NOT NULL,
    price REAL DEFAULT(0),
    media TEXT NOT NULL,
    total INTEGER DEFAULT(0),
    is_published BOOLEAN DEFAULT (false),
    name_en TEXT NOT NULL,
    name TEXT NOT NULL,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);
""")
conn.commit()
cur.execute("""
CREATE TABLE IF NOT EXISTS order_items(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    total INTEGER DEFAULT(0),
    FOREIGN KEY (order_id) REFERENCES orders(id)
);
""")
conn.commit()
cur.execute("""
CREATE TABLE IF NOT EXISTS orders(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    boot_user_id TEXT NOT NULL,
    date_create INTEGER NOT NULL,
    status_id INTEGER NOT NULL,
    invoice_id TEXT NOT NULL,
    FOREIGN KEY (status_id) REFERENCES statuses(id)
);
""")
conn.commit()
cur.execute("""
CREATE TABLE IF NOT EXISTS statuses(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
);
""")
conn.commit()
cur.execute("""
CREATE TABLE IF NOT EXISTS bot_users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    is_blocked BOOLEAN DEFAULT (false),
    balance INTEGER NOT NULL,
    language_id INTEGER NOT NULL,
    FOREIGN KEY (language_id) REFERENCES languages(id)
);
""")
conn.commit()
cur.execute("""
CREATE TABLE IF NOT EXISTS invoices(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bot_user_id TEXT NOT NULL,
    date_create INTEGER NOT NULL,
    total INTEGER DEFAULT(0),
    status_id INTEGER NOT NULL,
    FOREIGN KEY (status_id) REFERENCES statuses(id)
);
""")
conn.commit()
cur.execute("""
CREATE TABLE IF NOT EXISTS languages(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    language_code TEXT NOT NULL
);
""")
conn.commit()