from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

# Register your models here.
from .models import Category, HomePageSlider, NewsLetter

admin.site.register(NewsLetter)

admin.site.register(HomePageSlider)

admin.site.register(
	Category, 
	DraggableMPTTAdmin,
	list_display=(
        'tree_actions',
        'indented_title',
        # ...more fields if you feel like it...
    ),
    list_display_links=(
        'indented_title',
    ),
    )


