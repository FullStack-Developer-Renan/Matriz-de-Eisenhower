from app import db
from sqlalchemy.sql.sqltypes import TEXT, VARCHAR

from sqlalchemy import Column, Integer



class CategoryModel(db.Model):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)

    name = Column(VARCHAR(100), nullable=False, unique=True)
    description = Column(TEXT)

    def __repr__(self):
        return f"{self.id}" + ',' + f"{self.name}"

    
