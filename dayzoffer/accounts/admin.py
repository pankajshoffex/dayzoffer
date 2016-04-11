from django.contrib import admin

# Register your models here.
from .models import City, UserProfile, Country, State, SellerUser

admin.site.register(SellerUser)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
admin.site.register(UserProfile)

