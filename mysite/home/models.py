from django.db import models

# Create your models here.

from django.db import models
from django.contrib import admin
from django.utils import timezone
import datetime


# The class `Question` defines a model with fields for question text and publication date, along with
# a method to check if the question was published recently.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        """
        The function `was_published_recently` checks if the publication date of an object is within the
        last 24 hours.
        :return: The method `was_published_recently` is returning a boolean value. It checks if the
        `pub_date` of the object is within the last 24 hours from the current time (`now`). If the
        `pub_date` is within the last 24 hours, it returns `True`, indicating that the object was
        published recently. Otherwise, it returns `False`.
        """
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.question_text


# The `Choice` class represents a choice option for a question with attributes like choice text and
# number of votes.
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
        """
        The above code snippet defines a Choice model with fields for choice text, votes, and a foreign
        key to a Question model.
        :return: The `__str__` method in the provided code snippet is returning the `choice_text`
        attribute of the Choice model instance. This method is used to define a human-readable
        representation of the object when it is printed or displayed as a string. In this case, it will
        return the `choice_text` value of the Choice instance.
        """
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


def was_published_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_date <= now
