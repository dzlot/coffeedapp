from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


import os
import uuid

RATING_CHOICES = (
	(0, 'None'),
	(1, '*'),
	(2, '**'),
	(3, '***'),
	(4, '****'),
	(5, '*****'),
	)

def upload_to_location(instance, filename):
    blocks = filename.split('.')
    ext = blocks[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    instance.title = blocks[0]
    return os.path.join('uploads/', filename)

# Create your models here.

class Location(models.Model):
	title = models.CharField(max_length=300)
	description = models.TextField(null=True, blank=True)
	address = models.TextField(null=True, blank=True)
	hours = models.TextField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	image_file = models.ImageField(upload_to=upload_to_location, null=True, blank=True)

	def get_absolute_url(self):
		return reverse(viewname="location_list", args=[self.id])

	def __unicode__(self):
		return self.title

	def get_average_rating(self):
        average = self.review_set.all().aggregate(Avg('rating'))['rating__avg']
        if average == None:
            return average
        else:
            return int(average)

class Review(models.Model):
	location = models.ForeignKey(Location)
	user = models.ForeignKey(User)
	description = models.TextField(null=True, blank=True)
	rating = models.IntegerField(choices=RATING_CHOICES)
	created_at = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return str(self.location) + ': ' + str(self.user) + ': ' + str(self.created_at)



