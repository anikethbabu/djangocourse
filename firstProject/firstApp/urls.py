from django.urls import path
from firstApp.views import display, displayDateTime

urlpatterns = [
    path('hello/', display),
    path('datetime/', displayDateTime),
]