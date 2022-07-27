from secrets import choice
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

priorities = (
    ('High Priority', 'High Priority'),
    ('Medium Priority', 'Medium Priority'),
    ('Low Priority', 'Low Priority'),
)

class Task(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    priority = models.CharField(max_length=50, choices=priorities)
    date_added = models.DateTimeField(auto_now=True)
    date_due = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Habits(models.Model):
    habit = models.CharField(max_length=100, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
