from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth import logout

# Create your views here.
from .forms import UserRegisterForm, SellerRegistration
from .models import City, UserProfile, SellerUser, State, Country

def log_out(request):
	logout(request)
	return HttpResponseRedirect("/")


def login_user(request):
	if not request.user.is_authenticated():
		if request.POST:

				username = request.POST.get('username')
				password = request.POST.get('password')

				user = authenticate(username=username, password=password)
				if user is not None:
					if user.is_active:
						login(request, user)
						try:
							seller_user = SellerUser.objects.get(user=user)
							if seller_user:
								return HttpResponseRedirect('/vendor/')
						except:
							return HttpResponseRedirect("/")
					else:
						messages.error(request, "Your account is not active.")
				else:
					messages.error(request, "Your Username and/or Password were incorrect")
	else:
		try:
			seller_user = SellerUser.objects.get(user=request.user)
			if seller_user:
				return HttpResponseRedirect('/vendor/')
		except:
			return HttpResponseRedirect("/")

	return render(request, "accounts/sign_in.html", { })


def vendor_login(request):
	if not request.user.is_authenticated():
		if request.POST:
				username = request.POST.get('username')
				password = request.POST.get('password')
				print username, password
				user = authenticate(username=username, password=password)
				if user is not None:
					if user.is_active:
						login(request, user)
						# print request.GET.get('next')
						# if request.GET.get('next') is not None or request.GET.get('next') != 'None':
						# 	print request.GET.get('next')
						# 	return HttpResponseRedirect(request.GET.get('next'))
						# else:
						# 	print request.GET.get('next')
						return HttpResponseRedirect("/vendor/")
					else:
						messages.error(request, "Your account is not active.")
				else:
					messages.error(request, "Your Username and/or Password were incorrect")
	else:
		return HttpResponseRedirect("/vendor/")

	return render(request, "accounts/vendor_login.html", { })


def user_registration(request):
	if not request.user.is_authenticated():
		if request.method == "POST":
			form = UserRegisterForm(request.POST)
			if form.is_valid():
				full_name = form.cleaned_data.get("full_name")
				email = form.cleaned_data.get("email")
				password = form.cleaned_data.get("password1")
				city = form.cleaned_data.get("city")
				city_obj = City.objects.get(title=city)
				location_aria = form.cleaned_data.get("location_aria")
				mobile_no = form.cleaned_data.get("mobile_no")
				user = User.objects.create_user(username=email, first_name=full_name)
				user.set_password(password)
				user.save()
				uprofile = UserProfile.objects.create(user=user, city=city_obj)
				uprofile.location_aria = location_aria
				uprofile.mobile_no = mobile_no
				uprofile.save()
				return HttpResponseRedirect(reverse("accounts:signin"))
		else:
			form = UserRegisterForm()
	else:
		return HttpResponseRedirect("/")
	return render(request, "accounts/register.html", {'form': form})

def vender_registration(request):
	countries = Country.objects.all()
	states = State.objects.all()
	cities = City.objects.all()
	if request.method == "POST":
		firm_name = request.POST.get("firm_name")
		email = request.POST.get("email")
		password = request.POST.get("password1")
		city = request.POST.get("city")
		state = request.POST.get("state")
		country = request.POST.get("country")
		location_aria = request.POST.get("location_aria")
		mobile = request.POST.get("mobile")
		address = request.POST.get("address")
		lattitude = request.POST.get("lattitude")
		longitute = request.POST.get("longitute")
		pincode = request.POST.get('pincode')
		user = User.objects.create_user(username=email)
		user.set_password(password)
		user.save()
		country_obj = Country.objects.get(title=country)
		state_obj = State.objects.get(country=country_obj)
		city_obj = City.objects.get(title=city)
		seller = SellerUser.objects.create(user=user, country=country_obj, state=state_obj, city=city_obj)
		seller.firm_name = firm_name
		seller.address = address
		seller.mobile = mobile
		seller.pincode = pincode
		seller.location_aria = location_aria
		if lattitude:
			seller.lattitude = lattitude

		if longitute:
			seller.longitute = longitute

		seller.save()

		return HttpResponseRedirect("/accounts/vendor_login")
	context = {
		'countries': countries,
		'states': states,
		'cities': cities
	}

	return render(request, "accounts/vender_register.html", context)


