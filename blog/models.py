from django.db import models
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.CharField(max_length=255)
    draft = models.TextField(null=False)
    published_date = models.DateField()
    author = models.CharField(max_length=255)
    url = models.CharField(max_length=255, null=True, validators=[URLValidator()])

    def __str__(self):
        return f"{self.title}"