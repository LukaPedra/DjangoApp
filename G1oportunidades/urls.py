from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [

	url(r'^menu/', views.menu, name="menu"),
	url(r'^CreateProfile/', views.CreateProfile, name="CreateProfile"),
]