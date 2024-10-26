from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import date

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)

    orders = relationship('Orders', back_populates='user')

# Define the Products table
class Products(Base):
    __tablename__ = 'products'
    
    product_id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String, nullable=False)
    price = Column(Float, nullable=False)

    # Relationship to OrderDetails (one-to-many)
    order_details = relationship('OrderDetails', back_populates='product')

# Define the Orders table
class Orders(Base):
    __tablename__ = 'orders'
    
    order_id = Column(Integer, primary_key=True, autoincrement=True)
    order_date = Column(Date, nullable=False)
    user_id = Column(Integer, ForeignKey('users.user_id', ondelete='CASCADE'))

    # Relationship to Users (many-to-one)
    user = relationship('Users', back_populates='orders')

    # Relationship to OrderDetails (one-to-many)
    order_details = relationship('OrderDetails', back_populates='order')

class OrderDetails(Base):
    __tablename__ = 'order_details'
    
    order_detail_id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.order_id', ondelete='CASCADE'))
    product_id = Column(Integer, ForeignKey('products.product_id', ondelete='CASCADE'))
    quantity = Column(Integer, nullable=False)

    # Relationship to Orders (many-to-one)
    order = relationship('Orders', back_populates='order_details')

    # Relationship to Products (many-to-one)
    product = relationship('Products', back_populates='order_details')
