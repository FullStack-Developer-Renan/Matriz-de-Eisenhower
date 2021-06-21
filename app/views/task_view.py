from app.exc.status_option import StatusOptionsError
from app.services.task_service import create_task
from flask import Blueprint, request

from app.services.task_service import create_task
from app.exc import (
    MissingKeyError,
    RequiredKeyError,
)
from http import HTTPStatus

bp = Blueprint("bp_task_route", __name__)


@bp.route("/task", methods=["POST"])
def create():
    data = request.get_json()
    try:
        return create_task(data), HTTPStatus.CREATED

    except MissingKeyError as e:
        return e.message

    except StatusOptionsError as e:
        return e.message


