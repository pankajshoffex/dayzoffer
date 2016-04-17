from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from vendor.forms import ProductForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# Create your views here.
from .models import Product
from accounts.models import SellerUser
from accounts.forms import SellerRegistration
from vendor.mixins import LoginRequiredMixin
import datetime


@login_required(login_url='/accounts/vendor_login/')
def seller_index(request):
	now = datetime.datetime.today()
	seller_user = SellerUser.objects.get(user=request.user)
	active = Product.objects.filter(user=seller_user, validity__lt=now).count()
	deactive = Product.objects.filter(user=seller_user, validity__gt=now).count()
	products = Product.objects.filter(user=seller_user).count()
	return render(request, "vendor/dashboard.html", {'active': active, 'deactive': deactive, 'products': products})

def seller_profile(request):
	return render(request, "vendor/seller_profile.html", {})


class ProductCreateView(LoginRequiredMixin, CreateView):
	form_class = ProductForm
	template_name = "vendor/product_form.html"
	success_url = "/vendor/"

	def get_seller_user(self):
		seller_user = SellerUser.objects.get(user=self.request.user)
		return seller_user

	def form_valid(self, form, *args, **kwargs):
		form.instance.user = self.get_seller_user()
		return super(ProductCreateView, self).form_valid(form, *args, **kwargs)



class ProductListView(LoginRequiredMixin, ListView):
	queryset = Product.objects.all()

	def get_context_data(self, *args, **kwargs):
		context = super(ProductListView, self).get_context_data(*args, **kwargs)
		now = datetime.datetime.today()
		try:
			seller_user = SellerUser.objects.get(user=self.request.user)
			expired_products = Product.objects.filter(validity__lt=now, user=seller_user)
			context['expired_products'] = expired_products
		except:
			return HttpResponseRedirect('/')
		
		return context
	def get_queryset(self):
		try:
			seller_user = SellerUser.objects.get(user=self.request.user)
		except:
			return HttpResponseRedirect('/')
		return super(ProductListView, self).get_queryset().filter(user=seller_user)



class ProductExpiredListView(LoginRequiredMixin, ListView):
	template_name = "vendor/product_expired_list.html"
	now = datetime.datetime.today()
	queryset = Product.objects.filter(validity__gt=now)

	def get_queryset(self):
		seller_user = SellerUser.objects.get(user=self.request.user)
		return super(ProductExpiredListView, self).get_queryset().filter(user=seller_user)


class ProductDetailView(DetailView):
	model = Product



class ProductUpdateView(LoginRequiredMixin, UpdateView):
	model = Product
	form_class = ProductForm
	template_name_suffix = '_update_form'
	success_url = "/vendor/list"


class ProductDeleteView(LoginRequiredMixin, DeleteView):
	model = Product
	success_url = reverse_lazy('vendor:product_list')


class SellerUserUpdateView(LoginRequiredMixin, UpdateView):
	model = SellerUser
	form_class = SellerRegistration
	template_name = 'vendor/selleruser_form.html'
	success_url = "/vendor/user_update/"






