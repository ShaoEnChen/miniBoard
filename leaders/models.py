from django.db import models

class Record(models.Model):
	name = models.CharField(max_length=100)
	height = models.FloatField()
	def __unicode__(self):
		return "%s %scm" % (self.name, self.height)