from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Category, HomePageSlider, NewsLetter
from django.http import HttpResponseRedirect
from django.contrib import messages

from vendor.models import Product

# Create your views here.
import datetime



class HomeListView(ListView):
	model = Product
	template_name = "home.html"

	def get_context_data(self, *args, **kwargs):
		context = super(HomeListView, self).get_context_data(*args, **kwargs)
		# for Latest offers display
		now = datetime.datetime.today()
		latest_offers = Product.objects.filter(validity__gt=now).order_by('-validity')[:8]
		context['latest_offers'] = latest_offers
		# Homepage slider
		home_slider = HomePageSlider.objects.filter(active=True)
		context['home_slider'] = home_slider
		# Best Offers
		best_offer = Product.objects.filter(validity__gt=now).order_by('?')[:10]
		context['best_offer'] = best_offer
		return context

class CategoryDetailView(DetailView):
	model = Category
	template_name = "offers/category_detail.html"

	def get_context_data(self, *args, **kwargs):
		context = super(CategoryDetailView, self).get_context_data(*args, **kwargs)
		obj = self.get_object()
		now = datetime.datetime.today()
		offer_list = Product.objects.filter(validity__gt=now, category=obj)
		context['offer_list'] = offer_list
		# subcategory
		subcategory = obj.get_children()
		context['subcategory'] = subcategory
		return context



class OfferDetailView(DetailView):
	model = Product
	template_name = "offers/product_detail.html"

	def get_context_data(self, *args, **kwargs):
		context = super(OfferDetailView, self).get_context_data(*args, **kwargs)
		obj = self.get_object()
		try:
			category = Category.objects.get(name=obj.category.name)
		except:
			pass
		now = datetime.datetime.today()
		offer_list = Product.objects.filter(validity__gt=now, category=category).order_by('?')
		context['offer_list'] = offer_list
		# subcategory
		subcategory = obj.category.get_children()
		context['subcategory'] = subcategory
		return context

def newsletter(request):
	email = request.POST.get('news-email')
	if email:
		try:
			obj, cond = NewsLetter.objects.get_or_create(email=email)
			if cond:
				messages.success(request, "Thank You for subscriptions..")
			else:
				messages.success(request, "You are already subscribed user..")
		except:
			pass

	return HttpResponseRedirect('/')

