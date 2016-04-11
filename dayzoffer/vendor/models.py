from __future__ import unicode_literals

from django.db import models
from django.utils.text import slugify
from mptt.models import TreeForeignKey
from django.core.urlresolvers import reverse

# Create your models here.
from offers.models import Category
from accounts.models import SellerUser
import datetime
from offers.thumbs import ImageWithThumbsField

class ProductQuerySet(models.query.QuerySet):
	def active(self):
		now = datetime.datetime.today()
		data = self.filter(validity__gt=now)
		return data
		# return self.filter(active=True)

class ProductManager(models.Manager):
	def get_queryset(self):
		return ProductQuerySet(self.model, using=self._db)

	def all(self, *args, **kwargs):
		return self.get_queryset().active()


def product_image_upload_to(instance, filename):
	title = instance.name
	slug = slugify(title)
	file_extention = filename.split(".")[1]
	new_filename = "%s-%s.%s" %(slug, instance.id, file_extention)
	return "offers/%s/%s" %(slug, new_filename)

class Product(models.Model):
	user = models.ForeignKey(SellerUser)
	name = models.CharField(max_length=120)
	offer = models.CharField(max_length=120)
	description = models.TextField()
	category = TreeForeignKey(Category)
	coupon_code = models.CharField(max_length=120, blank=True, null=True)
	link = models.URLField(max_length=200)
	image = ImageWithThumbsField(upload_to=product_image_upload_to, sizes=((200,200),(320,320),))
	validity = models.DateField(editable=True)
	timestamp = models.DateField(auto_now=True, auto_now_add=False)
	active = models.BooleanField(default=True)
	slug = models.SlugField(blank=True, null=True)


	objects = ProductManager()

	def __unicode__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("offers:offer-detail", kwargs={"slug": self.slug})

	def save(self, *args, **kwargs):
		super(Product, self).save(*args, **kwargs)
		slug = slugify(self.name)
		self.slug = "%s-%s" %(slug, self.pk)
		super(Product, self).save(*args, **kwargs)


