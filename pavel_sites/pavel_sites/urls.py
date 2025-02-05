from django.contrib import admin
from django.urls import path
from portofolio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name="homepage"),
    path('portfolio-details', views.porto_details, name="portfolio-details"),
]
