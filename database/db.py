from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func

import os


class Db:
    base = declarative_base()
    DIR_BASE = os.path.dirname('./')
    connect = 'sqlite:///' + os.path.join(DIR_BASE, 'expenses.db')
    
    engine = None
    Session = sessionmaker()

    def connect_db(self):
        self.engine = create_engine(self.connect, echo=True)
        self.base.metadata.create_all(self.engine)

    def instance_db(self):
        return self.Session(bind=self.engine)
    

class Expenses(Db.base):
    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Integer, nullable=False)
    category = Column(String, nullable=False)
    note = Column(String, nullable=True)
    create_at = Column(DateTime, server_default=func.now())
    update_at = Column(DateTime, server_default=func.now(), onupdate=func.now())



db = Db()
connect = db.connect_db()
sponsored = db.instance_db()