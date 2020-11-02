
from django.urls import path, include
from . import views
urlpatterns = [
   path('', views.index,name="ShopHome"),
   path('about/', views.about,name="About"),
   path('contact/', views.contact,name="Contact"),
   path('tracker/', views.tracker,name="Tracker"),
   path('search/', views.search,name="Search"),
   path("products/<int:myid>", views.products,name="products"),
   path('checkout/', views.checkout,name="Checkout"),
   path('programtest',views.programTest,name="programTest")
]
