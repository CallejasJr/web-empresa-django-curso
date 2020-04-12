from django.urls import path
from . import views
urlpatterns = [
	#Path services
	path('',views.services, name="services"),
]