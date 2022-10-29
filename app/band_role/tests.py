from django.test import TestCase
# from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
# from band_role.models import BandRole


BAND_ROLE_LIST_URL = reverse('band-role-list')


# Create your tests here.
class publicBandRoleApiTest(TestCase):
    """Test the Band Role api public"""
    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """Test that login is required for retrieving orders"""
        res = self.client.get(BAND_ROLE_LIST_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


# class privateOrderApiTest(TestCase):
#     """Test the authorized Order API"""
#     def setUp(self):
#         self.user = get_user_model().objects.create_user(
#             'test@gmail.com',
#             'testpass'
#         )
#         self.product = Product.objects.create(
#             name='MacBook M1',
#             user_id=self.user,
#             price=99.99,
#             quantity_in_stock=200
#         )
#         self.address = Address.objects.create(
#             company_name='Shop Rite',
#             contact_name='Andrew Smith',
#             contact_title='mr',
#             address='2 Broad Street',
#             city='London',
#             postal_code='23401',
#             phone='07034252738',
#             fax='23456',
#             user_id=self.user,
#         )
#         self.client = APIClient()
#         self.client.force_authenticate(self.user)

#     def test_retrieve_order(self):
#         """Test retrieve orders"""
#         user = self.user
#         product = self.product
#         address = self.address
#         Order.objects.create(
#             order_code='ABC-DEF-GH',
#             status=True,
#             product_id=product,
#             user_id=user,
#             address_id=address,
#             unit_price=product.price,
#             quantity=5,
#             note='My purchase'
#         )

#         Order.objects.create(
#             order_code='ABC-GH-JKL',
#             status=True,
#             product_id=product,
#             user_id=user,
#             address_id=address,
#             unit_price=product.price,
#             quantity=5,
#             note='My Goods'
#         )

#         res = self.client.get(ORDER_URL)

#         self.assertEqual(res.status_code, status.HTTP_200_OK)
#         self.assertContains(res, user.id)

#     def test_create_order_successful(self):
#         """Test user create order successful"""
#         payload = {
#             'order_code': 'ABC-GH-JKL',
#             'status': True,
#             'product_id': self.product.id,
#             'user_id': self.user.id,
#             'address_id': self.address.id,
#             'unit_price': self.product.price,
#             'quantity': 5,
#             'note': 'My Goods'
#         }
#         res = self.client.post(ORDER_URL, payload)

#         self.assertEqual(res.status_code, status.HTTP_201_CREATED)
