from django.conf.urls import url
from django.contrib import admin
from .views import login_user, user_registration, log_out, vender_registration, vendor_login

urlpatterns = [
    url(r'^signin/$', login_user, name="signin"),
    url(r'^vendor_login/$', vendor_login, name="vendor_login"),
    url(r'^register/$', user_registration, name="register"),
    url(r'^logout/$', log_out, name="logout"),
    url(r'^seller_register/$', vender_registration, name="seller-register"),
]