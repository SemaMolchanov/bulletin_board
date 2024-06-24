from rest_framework import serializers
from .models import Bulletin


class BulletinInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bulletin
        fields = ['title', 'author']


class BulletinResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bulletin
        fields = ['id', 'title', 'author', 'views', 'position']


