from django.contrib.auth import get_user_model
from rest_framework import viewsets

from . models import Profile
from . serializers import UserSerializer, ProfileSerializer

User = get_user_model()


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('pk')
    serializer_class = UserSerializer
