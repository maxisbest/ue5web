from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils import timezone

class ArticlePost(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True)
    depart = models.CharField(max_length=100)  # department: ue, python, 或者 ksp
    subject = models.CharField(max_length=100)  # 属于哪个话题, 001, 002...999
    chapter = models.CharField(max_length=100)  # 属于哪个章节, 001, 002...999
    img_path = models.CharField(max_length=100, null=True)  # 图片保存在 base_dir/article/static/ue/999/imgs 下
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return self.title

