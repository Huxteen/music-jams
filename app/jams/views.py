from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from jams import serializers
from utils.renderers import CustomRenderer
from jams.models import (Jam, JamBandRole, JamInvitation)
from band_role.models import BandRole, UserBandRole
from jams.exceptions import (
    PerformerExistValidation,
    JamJoinedAlreadyValidation,
    JamStartedAlreadyValidation)
from django.utils import timezone


class CreateJamAPIView(generics.CreateAPIView):
    """Manage data in the database"""

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Jam.objects.all().order_by('-id')
    serializer_class = serializers.JamSerializer
    renderer_classes = [CustomRenderer]

    def perform_create(self, serializer):
        """Create new Jam"""
        serializer.save(host=self.request.user)


class JamList(generics.ListAPIView):
    """Manage data in the database"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Jam.objects.all().order_by('-id')
    serializer_class = serializers.JamListSerializer
    renderer_classes = [CustomRenderer]

    def get_queryset(self):
        return Jam.objects.filter(
            host=self.request.user.id)


class JamDetail(generics.RetrieveUpdateDestroyAPIView):
    """Manage data in the database"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Jam.objects.all().order_by('-id')
    serializer_class = serializers.JamSerializer
    renderer_classes = [CustomRenderer]

    def get_queryset(self):
        return Jam.objects.filter(
            host=self.request.user.id)


class JamListAPiView(generics.ListAPIView):
    """List All Jam."""
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.JamListSerializer
    queryset = Jam.objects.all().order_by('-id')
    renderer_classes = [CustomRenderer]


class JamBandRoleList(generics.ListCreateAPIView):
    """Manage data in the database"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = JamBandRole.objects.all().order_by('-id')
    serializer_class = serializers.JamBandRoleCreateSerializer
    renderer_classes = [CustomRenderer]

    def get_queryset(self):
        jam_id = self.request.GET.get('jam')
        response = JamBandRole.objects.filter(performer=self.request.user.id)
        if jam_id:
            response = JamBandRole.objects.filter(jam=jam_id)
        return response

    def perform_create(self, serializer):
        """Create new JamBandRole"""
        band_role = self.request.POST.get('band_role')
        jam = self.request.POST.get('jam')
        serializer.save(
            jam=Jam(pk=int(jam)),
            band_role=BandRole(pk=int(band_role)),
        )


class JamBandRoleDetail(generics.RetrieveUpdateDestroyAPIView):
    """Manage data in the database"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = JamBandRole.objects.all().order_by('id')
    serializer_class = serializers.JamBandRoleCreateSerializer
    renderer_classes = [CustomRenderer]

    def perform_update(self, serializer):
        """Update new JamBandRole"""
        jam_id = self.kwargs['pk']
        queryset = JamBandRole.objects.filter(id=jam_id).first()
        role_list = list(UserBandRole.objects.values_list(
            'id', flat=True).filter(user_id=self.request.user.id))

        if (queryset.band_role.id in role_list) and not (queryset.performer):
            serializer.save(performer=self.request.user)
        else:
            raise PerformerExistValidation()


class StartJamDetail(generics.UpdateAPIView):
    """
        Manage data in the database.
        Start Jam
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Jam.objects.all().order_by('id')
    serializer_class = serializers.StartJamSerializer
    renderer_classes = [CustomRenderer]

    def perform_update(self, serializer):
        """Start Jam"""
        jam_id = self.kwargs['pk']
        queryset = Jam.objects.filter(
            host=self.request.user.id, id=jam_id).first()

        role_list = list(JamBandRole.objects.values_list(
            'performer', flat=True).filter(jam=jam_id))

        if ((queryset) and (queryset.start_at is None)
                and (None not in role_list)):
            serializer.save(
                start_at=timezone.now(),
                status=True)
        else:
            raise JamStartedAlreadyValidation()


class JamInvitationList(generics.ListCreateAPIView):
    """Manage data in the database"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = JamInvitation.objects.all().order_by('-id')
    serializer_class = serializers.JamInvitationSerializer
    renderer_classes = [CustomRenderer]

    def get_queryset(self):
        return JamInvitation.objects.filter(
            user=self.request.user.id).order_by('-id')

    def perform_create(self, serializer):
        """Create new Jam"""
        jam = self.request.POST.get('jam')
        queryset = JamInvitation.objects.filter(
            user=self.request.user.id, jam=jam).first()

        jam_query = Jam.objects.filter(id=queryset.jam.id).first()
        if jam_query.status:
            raise JamStartedAlreadyValidation()

        if queryset:
            raise JamJoinedAlreadyValidation()

        serializer.save(
            jam=Jam(pk=int(jam)),
            user=self.request.user)


class JamInvitationDetail(generics.DestroyAPIView):
    """
        Manage data in the database.
        Delete Jam Invitation
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Jam.objects.all().order_by('id')
    serializer_class = serializers.JamInvitationSerializer
    renderer_classes = [CustomRenderer]
