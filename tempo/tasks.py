import time

from celery import shared_task
from celery import Task

from keybert import KeyBERT
from db import db
from sqlalchemy import text

@shared_task(ignore_result=False)
def add(a: int, b: int) -> int:
    return a + b


@shared_task()
def block() -> None:
    time.sleep(5)


@shared_task(bind=True, ignore_result=False)
def process(self: Task, total: int) -> object:
    for i in range(total):
        self.update_state(state="PROGRESS", meta={"current": i + 1, "total": total})
        time.sleep(1)

    return {"current": total, "total": total}

@shared_task(ignore_result=False)
def keywords(sentences):
    kw_model = KeyBERT()
    words = kw_model.extract_keywords((" ").join(sentences))
    return words
