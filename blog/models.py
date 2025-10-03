from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # date created
    updated_at = models.DateTimeField(auto_now=True)     # date updated

    def __str__(self):
        return self.title
