"""URLconfig of the music app.
Different URL patterns for an app are typically specified in the following ways:
    - for function-based views:
        urlpatterns = [
            path('<URL segment>/', views.<the corresponding view function>, name='<the corresponding view name>'>
        ]
    - for class-based views:
        urlpatterns = [
            path('<URL segment>/', views.<the corresponding view class>.as_view(), name='<the corresponding view name>'>
        ]
"""
from django.urls import path

from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index')
]

