from app import db

from flask_sqlalchemy.model import Model


def verify_missing_key(data: dict, required_keys: list) -> list:
    data_keys = data.keys()

    return [key for key in required_keys if key not in data_keys]


def verify_recieved_key(data: dict, key_list: list) -> list:
    data_keys = data.keys()

    return [key for key in data_keys if key not in key_list]

def add_commit(model: Model) -> None:
    db.session.add(model)
    db.session.commit()
