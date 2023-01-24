from sqlalchemy import create_engine,Column,String,Integer,ForeignKey
engine =create_engine("mysql+pymysql://root:root@localhost/implenet",echo = True) 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
 
Base = declarative_base()
class rose(Base):
    __tablename__ = 'rose'
    id =Column(Integer,primary_key =True)
    name =Column(String(23))
    adress =Column(String(24))
    email =Column(String(34))
class Invoice(Base):
    __tablename__ ='invoice'
    id =Column(Integer,primary_key =True)
    custid =Column(Integer, ForeignKey('rose.id'))
    invoice =Column(Integer)
    rose = relationship("rose" ,back_populates ="invoices")
rose.invoices = relationship("Invoice", order_by = Invoice.id, back_populates = "rose")
Base.metadata.create_all(engine)