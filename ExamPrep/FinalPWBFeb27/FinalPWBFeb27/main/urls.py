from django.urls import path

from FinalPWBFeb27.main.views.album import album_add_view, album_edit_view, album_delete_view, album_details_view
from FinalPWBFeb27.main.views.generic import home_view
from FinalPWBFeb27.main.views.profile import profile_details_view, profile_delete_view

urlpatterns = [
    path('', home_view, name='home'),
    path('album/add/', album_add_view, name='add album'),
    path('album/details/<int:pk>/', album_details_view, name='album details'),
    path('album/edit/<int:pk>/', album_edit_view, name='edit album'),
    path('album/delete/<int:pk>/', album_delete_view, name='delete album'),
    path('profile/details/', profile_details_view, name='profile details'),
    path('profile/delete/', profile_delete_view, name='delete profile'),
]
