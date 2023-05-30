from django.urls import path
from blog import views

urlpatterns = [
    path('', views.home, name="home"),
    path('blog/', views.blog, name="blog"),
    path('search/', views.search, name="search"),
    path('blogpost/<str:slug>', views.blogpost, name="home"),
    path('contact/', views.contact, name="contact"),
]
