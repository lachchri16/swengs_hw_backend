from django.contrib.auth.decorators import permission_required
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.http import HttpResponse
# from drf_yasg.utils import swagger_auto_schema
from rest_framework import views
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

from backend.yamod.models import Artist, Song, Label

from backend.yamod.serializers import ArtistFormSerializer, ArtistOptionSerializer, SongListSerializer, \
    SongFormSerializer, \
    LabelOptionSerializer


# test #

# list methods #

@api_view(['GET'])
def labels_option_list(request):
    labels = Label.objects.all()
    serializer = LabelOptionSerializer(labels, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def artist_option_list(request):
    artist = Artist.objects.all()
    serializer = ArtistOptionSerializer(artist, many=True)
    return Response(serializer.data)


@api_view(['GET'])
# @permission_required('yamod.view_movie', raise_exception=True)
def song_list(request):
    songs = Song.objects.all()
    serializer = SongListSerializer(songs, many=True)
    return Response(serializer.data)


# list methods end #

# song form CRUD #

@api_view(['GET'])
# @permission_required('yamod.view_movie', raise_exception=True)
def song_form_get(request, pk):
    try:
        song = Song.objects.get(pk=pk)
    except Song.DoesNotExist:
        return Response({'error': 'Song does not exist.'}, status=404)

    serializer = SongFormSerializer(song)
    return Response(serializer.data)


@api_view(['POST'])
# @permission_required('yamod.add_movie', raise_exception=True)
def song_form_create(request):
    serializer = SongFormSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['PUT'])
# @permission_required('yamod.change_movie', raise_exception=True)
def song_form_update(request, pk):
    try:
        song = Song.objects.get(pk=pk)
    except Song.DoesNotExist:
        return Response({'error': 'Song does not exist.'}, status=404)

    serializer = SongFormSerializer(song, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
# @permission_required('yamod.delete_movie', raise_exception=True)
def song_delete(request, pk):
    try:
        song = Song.objects.get(pk=pk)
    except Song.DoesNotExist:
        return Response({'error': 'Song does not exist.'}, status=404)
    song.delete()
    return Response(status=204)


# song CRUD end #

# artist form CRUD #

@api_view(['GET'])
# @permission_required('yamod.view_movie', raise_exception=True)
def artist_form_get(request, pk):
    try:
        artist = Artist.objects.get(pk=pk)
    except Artist.DoesNotExist:
        return Response({'error': 'Artist does not exist.'}, status=404)

    serializer = ArtistFormSerializer(artist)
    return Response(serializer.data)


@api_view(['POST'])
# @permission_required('yamod.add_movie', raise_exception=True)
def artist_form_create(request):
    serializer = ArtistFormSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['PUT'])
# @permission_required('yamod.change_movie', raise_exception=True)
def artist_form_update(request, pk):
    try:
        artist = Artist.objects.get(pk=pk)
    except Artist.DoesNotExist:
        return Response({'error': 'Artist does not exist.'}, status=404)

    serializer = ArtistFormSerializer(artist, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
# @permission_required('yamod.delete_movie', raise_exception=True)
def artist_delete(request, pk):
    try:
        artist = Artist.objects.get(pk=pk)
    except Artist.DoesNotExist:
        return Response({'error': 'Artist does not exist.'}, status=404)
    artist.delete()
    return Response(status=204)

# artist form CRUD end #
