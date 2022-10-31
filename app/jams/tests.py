from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from band_role.models import BandRole
from jams.models import Jam, JamBandRole, JamInvitation


USER_JAM_LIST_URL = reverse('users-jam-list')
USER_CREATE_JAM_URL = reverse('user-create-jam')
LIST_ALL_JAM_URL = reverse('list-all-jam')
LIST_JAM_BAND_ROLE_URL = reverse('list-jam-band-role')
USER_START_JAM_URL = reverse('user-start-jam', args=[1])
USER_JOIN_JAM_URL = reverse('user-join-jam')
JAM_BAND_ROLE_DETAIL_URL = reverse('jam-band-role-detail', args=[1])


# Create your tests here.
class publicJamApiTest(TestCase):
    """Test the Jam api public"""
    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """Test that login is required for retrieving Jams"""
        res = self.client.get(USER_CREATE_JAM_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class privateBandRoleApiTest(TestCase):
    """Test the authorized Band Role API"""
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            'test@gmail.com',
            'testpass'
        )

        self.user_2 = get_user_model().objects.create_user(
            'test2@gmail.com',
            'testpass'
        )

        self.user_3 = get_user_model().objects.create_user(
            'test3@gmail.com',
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

        self.band_role_2 = BandRole.objects.create(
            type='Drummer',
            user_id=self.admin_user,
        )

        self.jams = Jam.objects.create(
            name='Testing Testing',
            status=False,
            description='This is test case',
            location='Lagos, Nigeria',
            event_date='2022-10-31T10:53:18.198Z',
            is_public=True,
            host=self.user,
        )

        self.jam_invitation = JamInvitation.objects.create(
            jam=self.jams,
            user=self.user,
        )

        self.client = APIClient()
        self.client.force_authenticate(self.user)
        self.client.force_authenticate(self.admin_user)

    def test_retrieve_users_jams(self):
        """Test retrieve users jams"""
        res = self.client.get(USER_JAM_LIST_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_jams_successful(self):
        """Test admin create band role successful"""
        payload = {
            "name": "Testing 2",
            "status": False,
            "description": "this is a test case",
            "location": "Lagos",
            "event_date": "2022-10-31T10:53:18.198Z",
            "start_at": "2022-10-31T10:53:18.198Z",
            "is_public": True,
            "host": self.user,
            "jam_band_role": [
                {"band_role": self.band_role.id},
                {"band_role": self.band_role_2.id},
            ]
        }
        res = self.client.post(USER_CREATE_JAM_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data['name'], payload['name'])
        self.assertEqual(res.data['is_public'], payload['is_public'])

    def test_retrieve_all_jams(self):
        """Test retrieve all jams"""
        res = self.client.get(LIST_ALL_JAM_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_add_band_role_to_jams_successful(self):
        """Test admin create band role successful"""
        role_payload = {
            "jam": self.jams.id,
            "band_role": self.band_role.id,
        }
        res_role = self.client.post(LIST_JAM_BAND_ROLE_URL, role_payload)
        self.assertEqual(res_role.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res_role.data['jam'], role_payload['jam'])
        self.assertEqual(res_role.data['band_role'], role_payload['band_role'])

    def test_retrieve_band_role_for_jams_successful(self):
        """Test retrieve band role for jams"""
        JamBandRole.objects.create(
            jam=self.jams,
            band_role=self.band_role,
        )
        JamBandRole.objects.create(
            jam=self.jams,
            band_role=self.band_role_2,
        )
        res = self.client.get(LIST_JAM_BAND_ROLE_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_retrieve_all_jams_user_joins(self):
        """Test retrieve all jams"""
        res = self.client.get(USER_JOIN_JAM_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
