from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='listings'),
    #listing/123    views.py里 def listing(request, listing_id): 需要传入listing_id
    path('<int:listing_id>', views.listing, name='listing'),     
    path('search', views.search, name='search'),
]