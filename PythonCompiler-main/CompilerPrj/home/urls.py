from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.index, name="indexpage"),
	path('runcode', views.runcode, name="runcode"),
]
