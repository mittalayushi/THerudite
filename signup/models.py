from __future__ import unicode_literals

from django.db import models
from PIL import Image
from djangotoolbox.fields import ListField


# class Post(models.Model):
#     title = models.CharField()
#     text = models.TextField()
#     tags = ListField()
#     comments = ListField()

class User(models.Model):
	name=models.CharField(max_length=200)
	image=models.ImageField(null=True, upload_to='.')
	email=models.EmailField()
	id_token=models.CharField(max_length=1000)