from app.services.task_category_service import create_task_category

from flask import Blueprint, request
from http import HTTPStatus

bp = Blueprint("bp_char_tc_route", __name__)


@bp.route("/task_category", methods=["POST"])
def create():
    data = request.get_json()

    return create_task_category(data), HTTPStatus.CREATED
