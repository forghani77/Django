from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Course(models.Model):
	text = models.CharField(max_length=255)
	date = models.DateTimeField()
	amount = models.FloatField()
	user = models.ForeignKey(User, on_delete=models.PROTECT)
	def __unicode__(self):
		return "Mathematics"

class Mark(models .Model):
	text = models.CharField(max_length=255)
	date = models.DateTimeField()
	amount = models.FloatField()
	user = models.ForeignKey(User, on_delete=models.PROTECT)
	def __unicode__():
		return "18.5"
