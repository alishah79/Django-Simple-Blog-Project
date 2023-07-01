from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.category_name
    
    class Meta:
        verbose_name_plural = 'Categories'


class Post(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    text = models.TextField(default='Please enter yout text here...')
    categoties = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    text = models.TextField(blank=False)
    posts = models.ForeignKey(to=Post, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.text[:7]