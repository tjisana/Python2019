from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
