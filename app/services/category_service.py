from app.models.eisenhower_model import EisenhowerModel
from app.models.task_category_model import TaskCategoryModel
from app import db
from app.models.task_model import TaskModel
from app.exc import (
    MissingKeyError,
)
from app.models import CategoryModel
from .helpers import verify_missing_key, add_commit


def create_category(data: dict):
    key_list = ["name"]

    if verify_missing_key(data, key_list):
        raise MissingKeyError(data, key_list)

    
    new_category = CategoryModel(**data)

    add_commit(new_category)

    return {
        "id": new_category.id,
        "name": new_category.name,
        "description": new_category.description,
    }


def select_task_category():

    category_list: list[tuple[CategoryModel, TaskModel]] = (
        db.session.query(CategoryModel, TaskModel)
        .select_from(CategoryModel)
        .join(TaskCategoryModel)
        .join(TaskModel)
        .all()
    )


    task_list: list[tuple[TaskModel, CategoryModel]] = (
        db.session.query(TaskModel, CategoryModel)
        .select_from(TaskCategoryModel)
        .all()
    )

    return [
        {"category": {"name": category.name, "description": category.description, "task": [{"name": task.name, "description": task.description, "priority": EisenhowerModel.query.filter_by(id=task.eisenhower_id)[0].type}]}}
        for category, task in category_list
    ]
