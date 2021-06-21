from flask import Flask


def init_app(app: Flask):
    from .category_view import bp as bp_category
    from .task_view import bp as bp_task
    from .task_category_view import bp as bp_task_category

    app.register_blueprint(bp_category)
    app.register_blueprint(bp_task)
    app.register_blueprint(bp_task_category)

