from __future__ import unicode_literals

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.text import slugify
# Create your models here.



def homepage_image_upload_to(instance, filename):
	title = "homepageslider"
	slug = slugify(title)
	file_extention = filename.split(".")[1]
	new_filename = "%s-%s.%s" %(slug, instance.id, file_extention)
	return "home-slider/%s/%s" %(slug, new_filename)



class HomePageSlider(models.Model):
	caption1 = models.CharField(max_length=120)
	caption2 = models.CharField(max_length=120, blank=True)
	image = models.ImageField(upload_to=homepage_image_upload_to)
	active = models.BooleanField(default=True)

	def __unicode__(self):
		return self.caption1

def category_image_upload_to(instance, filename):
	title = instance.name
	slug = slugify(title)
	file_extention = filename.split(".")[1]
	new_filename = "%s-%s.%s" %(slug, instance.id, file_extention)
	return "offers/%s/%s" %(slug, new_filename)

class Category(MPTTModel):
	name = models.CharField(max_length=50, unique=True)
	parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
	slug = models.SlugField(blank=True, null=True)
	image = models.ImageField(upload_to=category_image_upload_to, blank=True, null=True)

	class MPTTMeta:
		order_insertion_by = ['name']

	def __unicode__(self):
		return self.name

	def save(self, *args, **kwargs):
		super(Category, self).save(*args, **kwargs)
		slug = slugify(self.name)
		self.slug = "%s-%s" %(slug, self.pk)
		super(Category, self).save(*args, **kwargs)	


class NewsLetter(models.Model):
	email = models.EmailField(blank=True, null=True)
	active = models.BooleanField(default=True)

	def __unicode__(self):
		return self.email



