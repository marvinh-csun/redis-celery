from celery import Celery
from celery import Task
from flask import Flask
from cache import redis


def celery_init_app(app: Flask) -> Celery:
    class FlaskTask(Task):
        def __call__(self, *args: object, **kwargs: object) -> object:
            with app.app_context():
                return self.run(*args, **kwargs)

    celery_app = Celery(app.name, task_cls=FlaskTask)
    celery_app.config_from_object(app.config["CELERY"])
    celery_app.set_default()
    app.extensions["celery"] = celery_app
    return celery_app

def create_app():


    from flask_json import FlaskJSON
    from api.routes  import api_blueprint
    from db import db
    app = Flask(__name__,template_folder='templates')
    app.register_blueprint(api_blueprint, url_prefix="/api")
    app.config['UPLOAD_FOLDER'] = '/tmp'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sail:password@host.docker.internal:13310/laravel'
    app.config.from_mapping(
        CELERY=dict(
            broker_url="redis://redis:6379",
            result_backend="redis://redis:6379",
            task_ignore_result=True,
        ),
    )
    celery_init_app(app)
    json = FlaskJSON()
    json.init_app(app)
    db.init_app(app)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0",debug=True)
