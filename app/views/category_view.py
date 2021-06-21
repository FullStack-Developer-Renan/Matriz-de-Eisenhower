from flask import Blueprint, request, jsonify

from app.services.category_service import create_category, select_task_category
from app.exc import (
    MissingKeyError,
    RequiredKeyError,
)
from http import HTTPStatus
from app import db

bp = Blueprint("bp_category_route", __name__)

@bp.route("/category", methods=["POST"])
def create():
    data = request.get_json()
    try:
        return create_category(data), HTTPStatus.CREATED

    except MissingKeyError as e:
        return e.message

    except RequiredKeyError as e:
        return e.message

@bp.route("/")
def get():
    return jsonify(select_task_category()), HTTPStatus.OK
    


