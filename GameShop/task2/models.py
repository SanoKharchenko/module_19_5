from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)  # название поста
    content = models.TextField()  # содержание поста
    created_at = models.DateTimeField(auto_now_add=True)  # автоматическое прописание времени публикации

