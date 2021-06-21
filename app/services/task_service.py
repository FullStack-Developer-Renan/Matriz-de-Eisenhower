from app.exc import (
    StatusOptionsError,
    GenderOptionsError,
    MissingKeyError,
)
from app.models import TaskModel, EisenhowerModel
from .helpers import verify_missing_key, add_commit


def eisenhower_classification(imp, urg):
    if imp == 1 and urg == 1:
        return EisenhowerModel.query.filter(
            EisenhowerModel.type == "Do It First"
        ).all()
    elif imp == 1 and urg == 2:
        return EisenhowerModel.query.filter(
            EisenhowerModel.type == "Delegate It"
        ).all()
    elif imp == 2 and urg == 1:
        return EisenhowerModel.query.filter(
            EisenhowerModel.type == "Schedule It"
        ).all()
    elif imp == 2 and urg == 2:
        return EisenhowerModel.query.filter(
            EisenhowerModel.type == "Delete It"
        ).all()

def create_task(data: dict):
    key_list = ["name"]

    if verify_missing_key(data, key_list):
        raise MissingKeyError(data, key_list)

    if data["importance"] > 2 or data["urgency"] > 2:
        raise StatusOptionsError(data)

    data["eisenhower_id"] = eisenhower_classification(data["importance"], data["urgency"])[0].id

    new_char = TaskModel(**data)

    add_commit(new_char)

    return {
        "id": new_char.id,
        "name": new_char.name,
        "description": new_char.description,
        "duration": new_char.duration,
        "eisenhower_classification": eisenhower_classification(data["importance"], data["urgency"])[0].type
    }
