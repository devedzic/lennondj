"""lennondj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from music import views

urlpatterns = [
    path('admin/', admin.site.urls),
]

# # The following lines have been put here first, before anything else has been added below,
# # and then they were moved to music/urls.py and music/urls.py was included here (otherwise an exception is raised)
# # urlpatterns += [
# #     path('', views.index, name='index')
# # ]
# urlpatterns += [
#     path('', views.IndexView.as_view(), name='index')
# ]

urlpatterns += [
    path('music/', include('music.urls'))
]

urlpatterns += [
    path('', RedirectView.as_view(url='music/'))
]
