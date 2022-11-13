from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("home/", views.home, name="home"),
    path('customers/', views.customers, name="customers"),
    path('about/', views.about, name='about'),
    path('updates/', views.updates, name='updates')

]


urlpatterns += staticfiles_urlpatterns()
