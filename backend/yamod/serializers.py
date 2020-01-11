from rest_framework import serializers
from .models import Song, Artist, Label


class SongListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'


class SongFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'


class LabelOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = '__all__'


class ArtistFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'


class ArtistOptionSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = Artist
        fields = ['id', 'name', 'stage_name']

    def get_name(self, obj):
        return ' '.join(filter(None, (obj.first_name, obj.last_name)))
