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


# urlpatterns = [
#     path('', views.index, name='index')
# ]
# from .views import BandDeleteView, MusicianDeleteView

urlpatterns = [
    path('', views.IndexView.as_view(), name='index')
]

urlpatterns += [
    path('bands/', views.BandListView.as_view(), name='band-list')
]

urlpatterns += [
    path('bands/<int:pk>/', views.BandDetailView.as_view(), name='band-detail')
]

urlpatterns += [
    path('musicians/', views.MusicianListView.as_view(), name='musician-list')
]

urlpatterns += [
    path('musicians/<int:pk>', views.MusicianDetailView.as_view(), name='musician-detail')
]

urlpatterns += [
    path('bands/create/', views.BandCreateView.as_view(), name='band-create'),
    path('bands/update/<int:pk>', views.BandUpdateView.as_view(), name='band-update'),
    path('bands/delete/<int:pk>', views.BandDeleteView.as_view(), name='band-delete')
]

urlpatterns += [
    path('musicians/create/', views.MusicianCreateView.as_view(), name='musician-create'),
    path('musicians/update/<int:pk>', views.MusicianUpdateView.as_view(), name='musician-update'),
    path('musicians/delete/<int:pk>', views.MusicianDeleteView.as_view(), name='musician-delete')
]

