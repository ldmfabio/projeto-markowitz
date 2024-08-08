from sqlalchemy import Column, Integer, String, Float, JSON
from db.base import Base

class UserModel(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    


class PortfolioModel(Base):
    __tablename__ = "portfolios"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, index=True)
    name = Column(String, index=True)
    description = Column(String)


class StockModel(Base):
    __tablename__ = "stocks"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    portfolio_id = Column(Integer, index=True)
    name = Column(String)
    price = Column(Float)
