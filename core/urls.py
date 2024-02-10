# comments/urls.py

from django.urls import path
from .views import *

urlpatterns = [
    path('post/<int:id>', postPage, name='post'),
    path('reply', replyPage, name='reply'),

    # Add other URLs as needed
]
