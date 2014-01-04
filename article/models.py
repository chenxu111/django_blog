from django.db import models
from time import time
def get_upload_file_name(instance,filename):
	mytime = str(time())
	mytime = mytime.replace('.','_')
	print "mytime:"+mytime + filename
	return "uploaded_files/%s%s" %(mytime,filename)
	# return str(time())

# Create your models here.
class Article(models.Model):
	title 		= models.CharField(max_length=200)
	body  		= models.TextField()
	pub_date	= models.DateTimeField('date published')
	likes 		= models.IntegerField(default=0)
	unlikes 	= models.IntegerField(default=0)
  	thumbnail	= models.FileField(upload_to = get_upload_file_name,blank=True)

	def __unicode__(self):
		return self.title
	
