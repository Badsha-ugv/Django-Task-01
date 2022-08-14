from django.contrib import admin
from .models import Question,Answer,TestFile
from django.contrib.auth.models import User

# Register your models here.

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(TestFile)