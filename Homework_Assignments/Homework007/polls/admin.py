from django.contrib import admin
from .models import Question, Choice

# Register the Question and Choice models with the admin site
admin.site.register(Question)
admin.site.register(Choice)
