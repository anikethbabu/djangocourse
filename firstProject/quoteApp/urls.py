from django.urls import path
from quoteApp.views import displayQuote

urlpatterns = [
    path('quote', displayQuote)
]