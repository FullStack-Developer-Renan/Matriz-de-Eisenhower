from app.models import EisenhowerModel

from app import db

def eisenhower_data():
    
    data = [{"type": "Do It First"}, {"type": "Delegate It"}, {"type": "Schedule It"}, {"type": "Delete It"}]

    db.session.add_all([EisenhowerModel(**dt) for dt in data])

    db.session.query(EisenhowerModel).filter(EisenhowerModel.id>4).delete()

    db.session.commit()

    
