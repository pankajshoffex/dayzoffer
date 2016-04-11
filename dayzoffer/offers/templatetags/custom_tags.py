from django import template
from offers.models import Category
from accounts.models import SellerUser, City

register = template.Library()

# @register.assignment_tag
# def set_logo():
# 	logo_data = UploadLogo.objects.all()
# 	logo = ""
# 	for i in logo_data:
# 		logo = i.logo.url
# 	return str(logo)

@register.assignment_tag
def set_node():
	nodes = Category.objects.all()
	return nodes

@register.assignment_tag
def set_city():
	cities = City.objects.all()
	return cities

@register.simple_tag
def get_offer_user(request):
	user = request.user
	try:
		offer_user = SellerUser.objects.get(user=user)
	except:
		raise Http404
	return offer_user

