from django.db import models

class Post(models.Model):
    class Meta():
        db_table = 'post'
    post_title = models.CharField(max_length=140)
    post_body = models.TextField()
    post_date = models.DateTimeField()
    post_like = models.IntegerField()
    post_img = models.ImageField(upload_to='media/images/', blank=True, null=True)

    def __str__(self):
        return self.post_title
