from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your models here.
class BandRole(models.Model):
    """Band Role Table"""
    type = models.CharField(max_length=255)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,
                                related_name='band_role_user_id')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type


class UserBandRole(models.Model):
    """User Band Role table"""
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,
                                related_name='user_band_roles')
    band_role_id = models.ForeignKey(BandRole, on_delete=models.CASCADE,
                                     related_name='band_role_id_user')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
