from __future__ import unicode_literals

from django.db import models
#from PIL import Image
from djangotoolbox.fields import ListField
from djangotoolbox.fields import EmbeddedModelField
#from bson.objectid import ObjectId

# class Post(models.Model):
#     title = models.CharField()
#     text = models.TextField()
#     tags = ListField()
#     comments = ListField()

class org(models.Model):
	name=models.CharField(max_length=200)
	person=models.CharField(max_length=100)
	email=models.EmailField()
	phone_no=models.IntegerField(null=True,blank=True)
	address=models.CharField(max_length=1000)
	schemes=ListField(EmbeddedModelField('scheme'))
	password=models.CharField(max_length=1000)

class scheme(models.Model):
	#_id=ObjectField(required=True, default=lambda:ObjectId())
	name=models.CharField(max_length=200)
	org_name=models.CharField(max_length=200)
	org_id=models.CharField(max_length=100)
	Rate=models.CharField(max_length=1000)
	description=models.CharField(max_length=5000)
	category=models.CharField(max_length=50)
	field=models.CharField(max_length=50)
	education=models.CharField(max_length=50)
	overseas=models.CharField(max_length=10)
	sports=models.CharField(max_length=20)
	income_ceiling=models.CharField(max_length=10)
	disability=models.CharField(max_length=5)
	gender=models.CharField(max_length=5)
	documents_req=models.CharField(max_length=200)
	tags=ListField()