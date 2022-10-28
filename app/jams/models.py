from django.db import models
from band_role.models import BandRole
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth import get_user_model
User = get_user_model()


# status, name, description, location, datetime, is_public, host, band_role(s)
# Create your models here.


def return_date_time():
    now = timezone.now()
    return now + timedelta(days=3)


class Jam(models.Model):
    """Jams table"""
    name = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=255)
    event_date = models.DateTimeField(default=return_date_time)
    is_public = models.BooleanField(default=False)
    host = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='jam_host')
    start_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class JamBandRole(models.Model):
    """Jam Band Role table"""
    jam = models.ForeignKey(Jam, on_delete=models.CASCADE,
                            related_name='jam_band_role')
    band_role = models.ForeignKey(BandRole, on_delete=models.CASCADE,
                                  related_name='band_role_jam')
    performer = models.ForeignKey(User, on_delete=models.CASCADE,
                                  null=True,
                                  related_name='performer_band_role')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class JamInvitation(models.Model):
    """Jam Invitation table"""
    jam = models.ForeignKey(Jam, on_delete=models.CASCADE,
                            related_name='jam_invitation')
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='user_invitation_jam')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
