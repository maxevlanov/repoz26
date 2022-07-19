from datetime import datetime

from sqlalchemy import (Column, SmallInteger,
                        ForeignKey, VARCHAR,
                        TIMESTAMP, DECIMAL)
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Category(Base):
    __tablename__: str = "categories"

    id = Column(SmallInteger, primary_key=True)
    parent_id = Column(SmallInteger, ForeignKey("categories.id", ondelete="CASCADE"))
    is_published = Column(Boolean)
    name_en = Column(VARCHAR(20), nullable=False)
    name = Column(VARCHAR(20), nullable=False)

class Product(Base):
    __tablename__: str = "products"

    id = Column(SmallInteger, primary_key=True)
    category_id = Column(SmallInteger, ForeignKey("categories.id", ondelete="CASCADE"), nullable=False)
    price = Column(DECIMAL(8, 2), default=0)
    media = Column(VARCHAR(30), nullable=False)
    total = Column(SmallInteger)
    is_published = Column(Boolean)
    name_en = Column(VARCHAR(20), nullable=False)
    name = Column(VARCHAR(24), nullable=False)

class Order_item(Base):
    __tablename__: str = "order_items"

    id = Column(SmallInteger, primary_key=True)
    order_id = Column(SmallInteger, ForeignKey("orders.id", ondelete="CASCADE"), nullable=False)
    product_id = Column(SmallInteger, ForeignKey("products.id", ondelete="CASCADE"), nullable=False)
    total = Column(SmallInteger)

class Order(Base):
    __tablename__: str = "orders"

    id = Column(SmallInteger, primary_key=True)
    bot_user_id = Column(SmallInteger, nullable=False)
    date_create = Column(TIMESTAMP, default=datetime.now())
    status_id = Column(SmallInteger, ForeignKey("statuses.id", ondelete="CASCADE"), nullable=False)
    invoice_id = Column(SmallInteger, ForeignKey("invoices.id", ondelete="CASCADE"), nullable=False)

class Status(Base):
    __tablename__: str = "statuses"

    id = Column(SmallInteger, primary_key=True)
    name = Column(VARCHAR(24), nullable=False)

class Bot_user(Base):
    __tablename__: str = "bot_users"

    id = Column(SmallInteger, primary_key=True)
    is_blocked = Column(Boolean)
    balance = Column(SmallInteger)
    language_id = Column(SmallInteger, ForeignKey("languages.id", ondelete="CASCADE"), nullable=False)

class Invoice(Base):
    __tablename__: str = "invoices"

    id = Column(SmallInteger, primary_key=True)
    bot_user_id = Column(SmallInteger, ForeignKey("bot_user.id", ondelete="CASCADE"), nullable=False)
    date_create = Column(TIMESTAMP, default=datetime.now())
    total = Column(SmallInteger)
    status_id = Column(SmallInteger, ForeignKey("statuses.id", ondelete="CASCADE"), nullable=False)

class Language(Base):
    __tablename__: str = "languages"

    id = Column(SmallInteger, primary_key=True)
    language_code = Column(VARCHAR(30), nullable=False)


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
    balance INTEGER DEFAULT(0),
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