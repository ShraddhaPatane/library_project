from django.db import models

class Book(models.Model):
    book_id = models.CharField(max_length=10, unique=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.title
