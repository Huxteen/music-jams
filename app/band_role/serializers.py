from rest_framework import serializers
from band_role.models import (BandRole, UserBandRole)


class BandRoleSerializer(serializers.ModelSerializer):
    """Serializer for Band Role objects"""

    class Meta:
        model = BandRole
        fields = ('id', 'type', 'is_active')
        read_only_fields = ('id',)


class UserBandRoleSerializer(serializers.ModelSerializer):
    """Serializer for User Band Role objects"""

    class Meta:
        model = UserBandRole
        fields = ('id', 'band_role_id', 'user_id')
        read_only_fields = ('id', 'user_id')


class ListUserBandRoleSerializer(serializers.ModelSerializer):
    """Serializer for User Band Role objects"""

    class Meta:
        model = UserBandRole
        fields = ('id', 'band_role_id',)
        read_only_fields = ('id',)
        depth = 1
