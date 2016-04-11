from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ProductListView.as_view(), name="product_list"),
    url(r'^profile/$', views.seller_profile, name="seller_profile"),
    url(r'^create/$', views.ProductCreateView.as_view(), name="product_create"),
    # url(r'^list/$', views.ProductListView.as_view(), name="product_list"),
    url(r'^expire_list/$', views.ProductExpiredListView.as_view(), name="product_expire_list"),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.ProductDetailView.as_view(), name="product_detail"),
    url(r'^update/(?P<pk>[0-9]+)/$', views.ProductUpdateView.as_view(), name="product_update"),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.ProductDeleteView.as_view(), name="product_delete"),
    url(r'^user_update/(?P<pk>[0-9]+)/$', views.SellerUserUpdateView.as_view(), name="seller_update"),   
]