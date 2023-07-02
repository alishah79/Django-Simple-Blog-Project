from django.utils.text import slugify
from django.db import models
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
import uuid


class BaseManager(models.Manager):

    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(is_deleted=False)
    def get_all(self) -> QuerySet:
        return super().get_queryset().all()
    

class BaseModel(models.Model):
    objects = BaseManager()
    created_at = models.DateTimeField(auto_now=True,)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Category(BaseModel):
    category_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.category_name
    
    class Meta:
        verbose_name_plural = 'Categories'


class Post(BaseModel):
    title = models.CharField(max_length=50, blank=False, null=False)
    text = models.TextField(default='Please enter yout text here...')
    categoties = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.title


class Comment(BaseModel):
    text = models.TextField(blank=False)
    posts = models.ForeignKey(to=Post, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.text[:7]