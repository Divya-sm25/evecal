# calendar_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Add a URL pattern for the calendar page
    path('', views.calendar_view, name='calendar_view'),
    path('api/events/', views.events_api, name='events_api'),
]
