
from django.urls import path, include
from . import views
urlpatterns = [
   path('', views.index,name="ShopHome"),
   path('about', views.about,name="About"),
   path('programtest',views.programTest,name="programTest")
]
