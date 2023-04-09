from rest_framework import serializers
from .models import *
from django_countries.serializer_fields import CountryField
from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers
from .models import *


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = '__all__'


class PropertySerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    country = CountryField(name_only=True)

    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Property
        fields = '__all__'

    def get_user(self, obj):
        return obj.user.username


class PropertyCreateSerializer(serializers.ModelSerializer):
    country = CountryField(name_only=True)
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model: property
        exclude = ["updated_at", "pkid"]


class PropertyViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = PropertyViews
        exclude = ["updated_at", "pkid"]
