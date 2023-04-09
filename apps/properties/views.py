from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import ProfileSerializer, UpdateProfileSerializer
from .signals import *
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response


# class PropertyViewSet(viewsets.ModelViewSet):
#     queryset = Property.objects.all()
#     serializer_class = PropertySerializer

#     def create(self, request, *args, **kwargs):
#         property_serializer = self.get_serializer(data=request.data)
#         property_serializer.is_valid(raise_exception=True)
#         property_instance = property_serializer.save()

#         photos_data = request.data.pop('photos', [])
#         create_photos.send(sender=self.__class__, instance=property_instance, created=True, photos_data=photos_data)

#         headers = self.get_success_headers(property_serializer.data)
#         return Response(property_serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class PropertyCreateAPIView(CreateAPIView):
    serializer_class = PropertySerializer

    def create(self, request, *args, **kwargs):
        photos_data = request.data.pop('photos', [])
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Create associated Photo objects
        property_instance = serializer.instance
        photo_serializer = PhotoSerializer(data=photos_data, many=True)
        photo_serializer.is_valid(raise_exception=True)
        photo_serializer.save(property=property_instance)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
