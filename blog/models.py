from django.db import models

class Post(models.Model):
    post_title = models.CharField(max_length=140)
    post_body = models.TextField()
    post_date = models.DateTimeField()

    def __str__(self):
        return self.post_title
