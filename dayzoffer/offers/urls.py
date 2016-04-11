from django.conf.urls import url
from .views import OfferDetailView, CategoryDetailView

urlpatterns = [
    url(r'^(?P<slug>[-\w]+)/$', CategoryDetailView.as_view(), name='category-detail'),
    url(r'^offer/(?P<slug>[-\w]+)/$', OfferDetailView.as_view(), name="offer-detail"),
]