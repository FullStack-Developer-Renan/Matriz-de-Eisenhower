from app import db
from sqlalchemy import Integer, Column, VARCHAR

class EisenhowerModel(db.Model):
    __tablename__ = "eisenhowers"

    id = Column(Integer, primary_key=True)
    
    type = Column(VARCHAR(100))

    def __repr__(self):
        return f"{self.id}" + ',' + f"{self.type}"
        
            