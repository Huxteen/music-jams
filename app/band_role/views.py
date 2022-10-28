from rest_framework import viewsets, mixins, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from band_role import serializers
from band_role.models import (BandRole, UserBandRole)
from utils.renderers import CustomRenderer


class BandRoleList(generics.ListCreateAPIView):
    """Manage data in the database"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsAdminUser)
    queryset = BandRole.objects.all()
    serializer_class = serializers.BandRoleSerializer
    renderer_classes = [CustomRenderer]

    def perform_create(self, serializer):
        """Create new Band Role"""
        serializer.save(user_id=self.request.user)


class BandRoleUserListAPiView(generics.ListAPIView):
    """List Band Role For User."""
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.BandRoleSerializer
    queryset = BandRole.objects.filter(is_active=True)
    renderer_classes = [CustomRenderer]


class BandRoleDetail(generics.RetrieveUpdateDestroyAPIView):
    """Manage data in the database"""
    authentication_classes = (TokenAuthentication, IsAdminUser)
    permission_classes = (IsAuthenticated,)
    queryset = BandRole.objects.all()
    serializer_class = serializers.BandRoleSerializer
    renderer_classes = [CustomRenderer]


class UserBandRoleList(generics.ListCreateAPIView):
    """Manage data in the database"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = UserBandRole.objects.all()
    serializer_class = serializers.UserBandRoleSerializer
    renderer_classes = [CustomRenderer]

    def get_queryset(self):
        return UserBandRole.objects.filter(
            user_id=self.request.user.id)

    def perform_create(self, serializer):
        """Create new Band Role"""
        serializer.save(user_id=self.request.user)
