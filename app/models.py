from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


# 定义customer模型
class Customer(Base):
    __tablename__ = 'customers'
    id = Column('id', String(20), primary_key=True)
    name = Column('name', String(50), nullable=False)
    password = Column('password', String(20), nullable=False)
    address = Column('address', String(100))
    phone = Column('phone', String(20))
    birthday = Column('birthday', String(20))


# 定义Goods模型
class Goods(Base):
    __tablename__ = 'goods'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(100), nullable=False)
    price = Column('price', Float)
    description = Column('description', String(200))
    brand = Column('brand', String(30))
    cpubrand = Column('cpu_brand', String(30))
    cputype = Column('cpu_type', String(30))
    memorycapacity = Column('memory_capacity', String(30))
    hdcapacity = Column('hd_capacity', String(30))
    cardmodel = Column('card_model', String(30))
    displaysize = Column('displaysize', String(30))
    image = Column('image', String(100))
    # 定义一对多的关系（Goods-> OrderLineItem）
    orderLineItems = relationship('OrderLineItem')


# 定义Orders模型
class Orders(Base):
    __tablename__ = 'orders'
    id = Column('id', String(20), primary_key=True)
    orderdate = Column('order_date', String(20))
    status = Column('status', Integer)  # 1待付款 0已付款
    total = Column('total', Float)
    # 定义一对多的关系（Orders-> OrderLineItem）
    orderLineItems = relationship('OrderLineItem')


# 定义OrderLineItems模型
class OrderLineItem(Base):
    __tablename__ = 'orderLineItems'
    id = Column('id', Integer, primary_key=True)
    quantity = Column('quantity', Integer)
    subtotal = Column('sub_total', Float)
    goodsid = Column('goodsid', ForeignKey('goods.id'))
    orderid = Column('orderid', ForeignKey('orders.id'))  # 1待付款 0已付款
    # 定义多对一的关系（OrderLineItem->Orders），backref表示反向关联
    orders = relationship('Orders', backref='OrderLineItem')  # Orders和OrderLineItem都是模型
    # 定义多对一的关系（OrderLineItem->Goods），backref表示反向关联
    goods = relationship('Goods', backref='OrderLineItem')  # Goods和OrderLineItem都是模型
