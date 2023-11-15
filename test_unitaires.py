import pytest
from django.contrib.auth.models import User
from  base.models import Product
from rest_framework.test import APIClient
from django.test import TestCase
from django.test import TestCase, Client
from django.urls import reverse

@pytest.mark.django_db
def test_discounted_price_calculation():
    user = User.objects.create(username='testuser')
    product = Product.objects.create(
        user=user,
        name='Test Product',
        price=100.00,
        discount=True,
        percentage=10.0,
    )

    assert product.discounted_price == 90.00



URL = "https://studitest.fly.dev"


class EndpointTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_getProducts(self):
        product_url =  URL + '/api/products/' 
        response = self.client.get(product_url)
        self.assertEqual(response.status_code, 200)


    def test_user_registration(self):
        user_register_url = URL + "/api/users/register/"
        data = {
            "name": "john Doe4",
            "email": "john4@gmail.com",
            "password": "john123"
        }
        response = self.client.post(user_register_url, data, format='json')
        self.assertEqual(response.status_code, 200) 



class TestURLs(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_admin_url(self):
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 302)  

    def test_product_api_url(self):
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, 200)

    def test_schema_url(self):
        response = self.client.get('/api/schema/')
        self.assertEqual(response.status_code, 200)

    def test_schema_docs_url(self):
        response = self.client.get('/api/schema/docs/')
        self.assertEqual(response.status_code, 200)