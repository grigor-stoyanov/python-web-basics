from django.shortcuts import render

from FinalPWBFeb27.main.forms.album import AlbumForm, DeleteAlbumForm
from FinalPWBFeb27.main.helpers import form_view
from FinalPWBFeb27.main.models import Album


def album_add_view(request):
    return form_view(request, AlbumForm, 'home', None, 'album/add-album.html')


def album_edit_view(request, pk):
    return form_view(request, AlbumForm, 'home', Album.objects.get(pk=pk), 'album/edit-album.html')


def album_delete_view(request, pk):
    return form_view(request, DeleteAlbumForm, 'home', Album.objects.get(pk=pk), 'album/delete-album.html')


def album_details_view(request, pk):
    album = Album.objects.get(pk=pk)
    ctx = {
        'album': album
    }
    return render(request, 'album/album-details.html', ctx)
