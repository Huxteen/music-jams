from rest_framework import serializers
from jams.models import (Jam, JamBandRole, JamInvitation)
from accounts.serializers import ListUserSerializer


class JamBandRoleCreateSerializer(serializers.ModelSerializer):
    """Serializer for JamBandRole objects"""

    class Meta:
        model = JamBandRole
        ordering = ['-id']
        read_only_fields = ('id', 'jam')
        exclude = ('created_at', 'updated_at', 'performer')


class JamSerializer(serializers.ModelSerializer):
    """Serializer for Jam objects"""
    jam_band_role = JamBandRoleCreateSerializer(many=True, required=False)

    class Meta:
        model = Jam
        ordering = ['-id']
        read_only_fields = ('id', 'start_at')
        fields = ('id',
                  'name',
                  'status',
                  'description',
                  'location',
                  'event_date',
                  'start_at',
                  'is_public',
                  'jam_band_role')

    def create(self, validated_data):
        """Create a new jam with the band role."""
        jam_band_role = validated_data.pop('jam_band_role', None)
        jam = Jam.objects.create(**validated_data)
        if jam_band_role:
            for jam_role in jam_band_role:
                JamBandRole.objects.create(jam=jam, **jam_role)
        return jam


class JamBandRoleListSerializer(serializers.ModelSerializer):
    """Serializer for JamBandRole objects"""
    performer = ListUserSerializer()

    class Meta:
        model = JamBandRole
        ordering = ['-id']
        read_only_fields = ('id',)
        fields = ('id', 'band_role', 'performer',)
        depth = 1


class JamListSerializer(serializers.ModelSerializer):
    """Serializer for Jam objects"""
    jam_band_role = JamBandRoleListSerializer(many=True)

    class Meta:
        model = Jam
        ordering = ['-id']
        read_only_fields = ('id', 'start_at')
        fields = ('id',
                  'name',
                  'status',
                  'description',
                  'location',
                  'event_date',
                  'start_at',
                  'is_public',
                  'jam_band_role')


class StartJamSerializer(serializers.ModelSerializer):
    """Serializer for Start Jam objects"""

    class Meta:
        model = Jam
        read_only_fields = ('id',
                            'created_at',
                            'updated_at',
                            'host',
                            'name',
                            'status',
                            'description',
                            'location',
                            'event_date',
                            'start_at',
                            'is_public')
        exclude = (
            'created_at',
            'updated_at',
            'host',
            'name',
            'status',
            'description',
            'location',
            'event_date',
            'start_at',
            'is_public')


# class JamBandRoleSerializer(serializers.ModelSerializer):
#     """Serializer for JamBandRole objects"""

#     class Meta:
#         model = JamBandRole
#         ordering = ['-id']
#         read_only_fields = ('id',)
#         exclude = ('created_at', 'updated_at', 'performer',)
#         # depth = 1

    # def update(self, instance, validated_data):
    #     """Update a performer"""
    #     validated_data.pop('band_role', None)
    #     validated_data.pop('jam', None)
    #     band_role = super().update(instance, validated_data)
    #     return band_role


class JamInvitationSerializer(serializers.ModelSerializer):
    """Serializer for Jam Invitation objects"""

    class Meta:
        model = JamInvitation
        ordering = ['-id']
        read_only_fields = ('id',)
        exclude = ('created_at', 'updated_at', 'user')
