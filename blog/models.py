from django.db import models

class BlogApp(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(max_length=15000)
    date = models.DateField()

    def __str__(self):
        return self.title

