from django.urls import path
from . import views


app_name = 'estimator'
urlpatterns = [
	path('', views.home, name='home'),
	path('dataset/', views.dataset, name='dataset'),
	path('predict/', views.predict, name='predict'),
]