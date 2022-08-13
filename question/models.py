from hashlib import blake2b
from operator import mod
import re
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    asked_by = models.ForeignKey(User, on_delete=models.CASCADE)
    question_text = models.TextField(blank=True)
    # and all other fields
    def __str__(self):
        return self.asked_by.username

class Answer(models.Model):
    answer_of = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField(blank=True)
    media = models.ImageField(upload_to='media/image',null=True,blank=True) 
    def __str__(self):
        return self.answer_text[:15] 