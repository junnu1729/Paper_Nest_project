from django.urls import path
from papernestapp import views
from .views import contact
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('about/',views.about,name="about"),
    path('contact/',contact,name="contact"),
    path('papers/', views.paper_list, name='paper_list'),
]