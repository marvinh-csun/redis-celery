from flask import Blueprint, request, render_template, abort, jsonify
from celery.result import AsyncResult
from werkzeug.utils import secure_filename
from cache import redis
import json
import os
from models import UserFavorite, User, Business
from db import db
from sqlalchemy.orm import aliased
from api.schema import UserSchema, BusinessSchema
import pickle
from sqlalchemy import text
import tasks
from keybert import KeyBERT
api_blueprint = Blueprint('api_blueprint', __name__ , template_folder='templates')

@api_blueprint.route("/blogs")
def index():
    statement = text(
            """
            SELECT * FROM blogs
            """
        )
    blogs = db.session.execute(statement,None)

    blogs = list(blogs)
    
    return render_template("blogs/index.jinja", blogs=blogs)

@api_blueprint.get("/result/<id>")
def result(id: str) -> dict[str, object]:
    result = AsyncResult(id)
    ready = result.ready()
    return {
        "ready": ready,
        "successful": result.successful() if ready else None,
        "value": result.get() if ready else result.result,
    }

@api_blueprint.post("/extract_keywords")
def extract_keywords():
    statement = text(
            """
            SELECT * FROM blogs
            """
        )
    blogs = db.session.execute(statement,None)

    blogs = [i._asdict() for i in blogs]

    sentences = [i["body"] for i in blogs]
    result = tasks.keywords.delay(sentences)
    return {"result_id": result.id}


@api_blueprint.post("/add")
def add() -> dict[str, object]:
    a = request.form.get("a", type=int)
    b = request.form.get("b", type=int)
    result = tasks.add.delay(a, b)
    return {"result_id": result.id}


@api_blueprint.post("/block")
def block() -> dict[str, object]:
    result = tasks.block.delay()
    return {"result_id": result.id}


@api_blueprint.post("/process")
def process() -> dict[str, object]:
    result = tasks.process.delay(total=request.form.get("total", type=int))
    return {"result_id": result.id}

