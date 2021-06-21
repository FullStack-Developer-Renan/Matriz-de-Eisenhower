from app.models.eisenhower_model import EisenhowerModel
from app import db
from app.models.category_model import CategoryModel
from app.models.task_model import TaskModel
from app.models.task_category_model import TaskCategoryModel as TCM


def create_task_category(data: dict) -> dict:
    category: CategoryModel = CategoryModel.query.filter_by(name=data["category_name"])
    task: TaskModel = TaskModel.query.filter_by(name=data["task_name"])
    eisenhower: EisenhowerModel = EisenhowerModel.query.filter_by(id=task[0].eisenhower_id)

    char_tc = TCM(task_id=task[0].id, category_id=category[0].id)

    db.session.add(char_tc)
    db.session.commit()

    return {
        "task": task[0].name,
        "category": category[0].name,
        "eisenhower_classification": eisenhower[0].type,
    }
