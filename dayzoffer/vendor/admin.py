from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'offer', 'coupon_code', 'link', 'product_image', 'active']
	list_filter = ['active']
	search_fields = ['name']
	class Meta:
		model = Product

	def product_image(self, obj):
		return mark_safe("""<img src="%s" width="74" height="74" />""" % obj.image.url)

admin.site.register(Product, ProductAdmin)

