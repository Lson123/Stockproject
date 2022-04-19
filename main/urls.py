from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('stockpicker/', views.stockPicker, name = 'stockpicker'),
    path('stocktracker/', views.stockTracker, name = 'stocktracker'),
    path('stockpredict/', views.stock_predict, name='stockpredict'),
    path('about/', views.about, name = 'about'),
]
