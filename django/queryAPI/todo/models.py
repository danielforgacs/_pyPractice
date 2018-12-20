from django.db import models

# Create your models here.
PRIORITY_CHOICES = [(1, 'High'), (2, 'Low')]

class Todo(models.Model):
    content = models.CharField(max_length=100)
    is_done = models.BooleanField(default=False)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    priority = models.IntegerField(choices=PRIORITY_CHOICES,
                                   default=1)