from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import gettext_lazy as _
from band_role.serializers import (UserBandRoleSerializer,
                                   ListUserBandRoleSerializer)
from band_role.models import UserBandRole
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user object."""
    user_band_roles = ListUserBandRoleSerializer(many=True)

    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'password', 'first_name', 'last_name',
                  'user_band_roles')
        read_only_fields = ('id',)
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def update(self, instance, validated_data):
        """Update a user setting the password correctly and return it"""
        password = validated_data.pop('password', None)
        validated_data.pop('user_band_roles', None)
        validated_data.pop('email', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()
        return user


class CreateUserSerializer(serializers.ModelSerializer):
    """Serializer for the user object."""
    user_band_roles = UserBandRoleSerializer(many=True, required=False)

    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'password', 'first_name', 'last_name',
                  'user_band_roles')
        read_only_fields = ('id',)
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """Create a new user with encrypted password and return it."""
        user_band_role = validated_data.pop('user_band_roles', None)
        user = get_user_model().objects.create_user(**validated_data)
        if user_band_role:
            for user_role in user_band_role:
                UserBandRole.objects.create(user_id=user, **user_role)
        return user


class ListUserSerializer(serializers.ModelSerializer):
    """Serializer for the user object."""
    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name')


class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user authentication objects"""
    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=True
    )

    def validate(self, attrs):
        """Validate and authenticate the user."""
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )
        if not user:
            msg = _('Email or Password do not match our record.')
            raise serializers.ValidationError(msg, code='authentication')

        attrs['user'] = user
        return attrs
