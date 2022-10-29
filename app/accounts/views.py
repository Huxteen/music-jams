from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from accounts import serializers
from utils.renderers import CustomRenderer


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = serializers.CreateUserSerializer
    renderer_classes = [CustomRenderer]


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user"""
    serializer_class = serializers.AuthTokenSerializer
    renderer_classes = [CustomRenderer]


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = serializers.UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    renderer_classes = [CustomRenderer]

    def get_object(self):
        """Retrieve and return authenticated user"""
        return self.request.user
