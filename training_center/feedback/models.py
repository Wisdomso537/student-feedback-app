from django.db import models

# Create your models here.


class Feedback(models.Model):
    student_name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
