import uuid

from django.db import models

# Create your models here.

class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, null=False, blank=False, editable=False)
    name = models.CharField(max_length=100,blank=False, null=False)
    country = models.CharField(max_length=100,blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

class Blog(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,null=False,blank=False,editable=False)
    author = models.ManyToManyField(Author,related_name="blog_authors",related_query_name="blog_author")
    title = models.CharField(max_length=200,blank=False, null=False)
    body = models.TextField(blank=False, null=False)

