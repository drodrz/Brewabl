from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string
from .models import Fermentable, Yeast, Hop, Misc, WaterProfile, Recipe

User = get_user_model()


class FermentableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fermentable
        fields = ('id', 'url', 'name', 'mfg', 'type', 'ppg', 'srm')
        read_only_fields = ('id', 'url')
        rw_fields = tuple(set(fields)-set(read_only_fields))

    def update(self, instance, validated_data):
        for field in self.Meta.rw_fields:
            setattr(instance, field, validated_data.get(field))

        instance.save()

        return instance


class HopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hop
        fields = ('id', 'url', 'name', 'type', 'weight', 'duration', 'aa')
        read_only_fields = ('id', 'url')
        rw_fields = tuple(set(fields)-set(read_only_fields))

    def update(self, instance, validated_data):
        for field in self.Meta.rw_fields:
            setattr(instance, field, validated_data.get(field))

        instance.save()

        return instance


class YeastSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Yeast
        fields = ('id', 'url', 'name', 'mfg', 'type', 'att_min', 'att_max')
        read_only_fields = ('id', 'url')
        rw_fields = tuple(set(fields)-set(read_only_fields))

    def update(self, instance, validated_data):
        for field in self.Meta.rw_fields:
            setattr(instance, field, validated_data.get(field))

        instance.save()

        return instance


class MiscSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = ('id', 'url', 'name', 'type')
        read_only_fields = ('id', 'url')
        rw_fields = tuple(set(fields)-set(read_only_fields))

    def update(self, instance, validated_data):
        for field in self.Meta.rw_fields:
            setattr(instance, field, validated_data.get(field))

        instance.save()

        return instance


class WaterProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WaterProfile
        fields = ('id', 'url', 'name', 'calcium', 'magnesium', 'sodium', 'chlorine', 'alkalinity', 'pH')
        read_only_fields = ('id', 'url')
        rw_fields = tuple(set(fields)-set(read_only_fields))

    def update(self, instance, validated_data):
        for field in self.Meta.rw_fields:
            setattr(instance, field, validated_data.get(field))

        instance.save()

        return instance


class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recipe
        fields = ('id', 'url', 'author', 'name', 'style', 'type', 'notes', 'fermentables', 'hops', 'yeast', 'misc',
                  'created', 'modified', 'original')
        read_only_fields = ('id', 'url', 'author', 'created', 'modified')

        rw_fields = tuple(set(fields)-set(read_only_fields))

    def update(self, instance, validated_data):
        for field in self.Meta.rw_fields:
            setattr(instance, field, validated_data.get(field))

        #TODO: Set time modified

        instance.save()

        return instance


class RecipeListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recipe
        fields = ('id', 'url', 'name', 'style')
        model = Recipe
