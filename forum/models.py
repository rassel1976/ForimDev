
from django.db import models

# Create your models here.

class Post(models.Model):
    class Meta:
        db_table = "post"
    post_name = models.CharField(max_length=255, verbose_name="Название поста")
    post_text = models.TextField(verbose_name="Текс Поста")
    post_time = models.DateTimeField(auto_now_add=True)
    post_user = models.CharField(max_length=255)

    def __str__(self):
        return self.post_name

class Comment(models.Model):
    class Meta:
        db_table = "comments"
    comment_text = models.TextField(verbose_name="Текст комментария")
    comment_post = models.ForeignKey(Post)
    comment_name = models.CharField(max_length=255)
