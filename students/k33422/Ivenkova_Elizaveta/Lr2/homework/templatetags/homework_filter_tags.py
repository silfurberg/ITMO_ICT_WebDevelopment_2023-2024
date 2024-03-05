from django import template
from homework import models
from django.db.models import QuerySet

register = template.Library()


@register.filter(name='get_not_submitted')
def get_not_submitted(stud_homework: QuerySet[models.StudentHomework]):
    return stud_homework.filter(answer='', mark__isnull=True)


@register.filter(name='get_submitted_not_graded')
def get_not_submitted_not_graded(stud_homework: QuerySet[models.StudentHomework]):
    return stud_homework.exclude(answer='').filter(mark__isnull=True)


@register.filter(name='get_graded')
def get_graded(stud_homework: QuerySet[models.StudentHomework]):
    return stud_homework.exclude(answer='').filter(mark__isnull=False)