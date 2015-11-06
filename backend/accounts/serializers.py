from django.contrib.auth import get_user_model, authenticate
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model

from rest_framework import serializers, exceptions
from .models import Profile

User = get_user_model()


class LoginSerializer(serializers.Serializer):
    username = serializers.EmailField(required=True, allow_blank=True)
    email = serializers.EmailField(required=True, allow_blank=False)
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if 'allauth' in settings.INSTALLED_APPS:
            from allauth.account import app_settings
            # Authentication through email
            if email and password:
                user = authenticate(email=email, password=password)
            else:
                msg = _('Must include "email" and "password".')
                raise exceptions.ValidationError(msg)

        # Did we get back an active user?
        if user:
            if not user.is_active:
                msg = _('User account is disabled.')
                raise exceptions.ValidationError(msg)
        else:
            msg = _('Unable to log in with provided credentials.')
            raise exceptions.ValidationError(msg)

        # If required, is the email verified?
        if 'rest_auth.registration' in settings.INSTALLED_APPS:
            from allauth.account import app_settings
            if app_settings.EMAIL_VERIFICATION == app_settings.EmailVerificationMethod.MANDATORY:
                email_address = user.emailaddress_set.get(email=user.email)
                if not email_address.verified:
                    raise serializers.ValidationError('E-mail is not verified.')

        attrs['user'] = user
        return attrs


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'url', 'picture', 'location', 'email_verified')
        read_only_fields = ('user', 'url', 'email_verified' )
        rw_fields = tuple(set(fields)-set(read_only_fields))

    def update(self, instance, validated_data):
        for field in self.Meta.rw_fields:
            setattr(instance, field, validated_data.get(field))

        instance.save()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = get_user_model()
        fields = ('id', 'url', 'name', 'email', 'username', 'profile')
        read_only_fields = ('id', 'url', 'email', 'username', 'profile')

