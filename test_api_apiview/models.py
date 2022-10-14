import uuid

from django.db import models

# Create your models here.
class AuthorApiView(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, null=False, blank=False, editable=False)
    name = models.CharField(max_length=100,blank=False, null=False)
    country = models.CharField(max_length=100,blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
