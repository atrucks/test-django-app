from celery import shared_task

from .models import Issue


@shared_task
def create_new_issue(name: str) -> None:
    Issue.objects.create(name=name)
