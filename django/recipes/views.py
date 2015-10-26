from django.contrib.auth import get_user_model
from django.db.models import Q

from rest_framework import viewsets

from . mixins import MultiSerializerViewSetMixin
from . models import Fermentable, Hop, Yeast, WaterProfile, Misc, Recipe
from . serializers import FermentableSerializer, HopSerializer, YeastSerializer, WaterProfileSerializer, MiscSerializer, \
    RecipeSerializer, RecipeListSerializer

User = get_user_model()


class RecipeViewSet(MultiSerializerViewSetMixin, viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    serializer_action_classes = {
        'list': RecipeListSerializer,
    }

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        return Recipe.objects.all()


class FermentableViewSet(viewsets.ModelViewSet):
    queryset = Fermentable.objects.all()
    serializer_class = FermentableSerializer


class HopViewSet(viewsets.ModelViewSet):
    queryset = Hop.objects.all()
    serializer_class = HopSerializer


class YeastViewSet(viewsets.ModelViewSet):
    queryset = Yeast.objects.all()
    serializer_class = YeastSerializer


class WaterProfileViewSet(viewsets.ModelViewSet):
    queryset = WaterProfile.objects.all()
    serializer_class = WaterProfileSerializer


class MiscViewSet(viewsets.ModelViewSet):
    queryset = Misc.objects.all()
    serializer_class = MiscSerializer
