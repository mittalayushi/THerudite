from __future__ import unicode_literals

from django.db import models
from PIL import Image
from djangotoolbox.fields import ListField
from djangotoolbox.fields import EmbeddedModelField
#from bson.objectid import ObjectId
# class Post(models.Model):
#     title = models.CharField()
#     text = models.TextField()
#     tags = ListField()
#     comments = ListField()

class User(models.Model):
	name=models.CharField(max_length=200)
	image=models.ImageField(null=True, upload_to='.')
	email=models.EmailField()
	d_o_b=models.CharField(max_length=11)
	gender=models.CharField(max_length=100)
	field=models.CharField(max_length=50)
	education=models.CharField(max_length=50)
	id_token=models.CharField(max_length=1000)
	overseas=models.CharField(max_length=10)
	tags=ListField()
	sports=models.CharField(max_length=20)
	resume = models.FileField(upload_to='./static/resumes')
	category=models.CharField(max_length=100)
	income_ceiling=models.CharField(max_length=100)
	physically_handicapped=models.CharField(max_length=10)
	physical_medical=models.FileField(upload_to='./static/medical')
	transcripts=models.FileField(upload_to='./static/trans')
	letter_of_recommendation=models.FileField(upload_to='./static/let_of_recom')
	lang_certri=models.FileField(upload_to='./static/lang_certi')
	state_of_pur=models.FileField(upload_to='./static/state_of_purp')
	score=models.FileField(upload_to='./static/scores')
	scholarship=ListField(EmbeddedModelField('Scholarship'))


class Scholarship(models.Model):
	identification=models.CharField(max_length=100)
	name=models.CharField(max_length=200)
	status=models.CharField(max_length=50)
	resubmission=models.CharField(max_length=100)

		