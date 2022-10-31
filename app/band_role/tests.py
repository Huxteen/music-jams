from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from band_role.models import BandRole, UserBandRole


BAND_ROLE_CREATE_LIST_URL = reverse('band-role-create-list')
LIST_ACTIVE_BAND_ROLE = reverse('list-all-active-band-role')
CREATE_USER_BAND_URL = reverse('create-user-band-role')
LIST_USER_BAND_URL = reverse('list-user-band-role')


# Create your tests here.
class publicBandRoleApiTest(TestCase):
    """Test the Band Role api public"""
    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """Test that login is required for retrieving Band Role"""
        res = self.client.get(BAND_ROLE_CREATE_LIST_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class privateBandRoleApiTest(TestCase):
    """Test the authorized Band Role API"""
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            'test@gmail.com',
            'testpass'
        )

        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@gmail.com',
            password='password123'
        )

        self.band_role = BandRole.objects.create(
            type='Vocalist',
            user_id=self.admin_user,
        )

        self.client = APIClient()
        self.client.force_authenticate(self.user)
        self.client.force_authenticate(self.admin_user)

    def test_retrieve_band_role(self):
        """Test retrieve BandRole"""
        admin_user = self.admin_user
        BandRole.objects.create(
            type='Drummer',
            user_id=admin_user,
        )

        res = self.client.get(BAND_ROLE_CREATE_LIST_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertContains(res, admin_user.id)

    def test_retrieve_user_band_role(self):
        """Test retrieve user BandRole"""
        user = self.user
        band_role = self.band_role
        UserBandRole.objects.create(
            user_id=user,
            band_role_id=band_role,
        )
        UserBandRole.objects.create(
            user_id=user,
            band_role_id=band_role,
        )
        res = self.client.get(LIST_USER_BAND_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_band_role_successful(self):
        """Test admin create band role successful"""
        payload = {
            'type': 'Vocalist',
            'user_id': self.admin_user,
            'is_active': True,
        }
        res = self.client.post(BAND_ROLE_CREATE_LIST_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data['type'], payload['type'])

    def test_create_user_band_role_successful(self):
        """Test user create add band role successful"""
        user = self.user
        band_role = self.band_role
        payload = {
            'user_id': user,
            'band_role_id': band_role.id,
        }
        res = self.client.post(CREATE_USER_BAND_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data['band_role_id'], payload['band_role_id'])
        self.assertEqual(res.data['band_role_id'], user.id)
