from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Company

class CompanyListTests(APITestCase):
    def setUp(self):
        self.url = reverse('company_list')

    def test_get_company_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_company(self):
        data = {'name': 'Nokia', 'phone': '0124578', 'email': "test@gmail.com", 'address': "Dhaka"}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Company.objects.count(), 1)
        self.assertEqual(Company.objects.get().name, 'Nokia')

class CompanyDetailTests(APITestCase):
    def setUp(self):
        self.company = Company.objects.create(name='Nokia', address='Test address')
        self.url = reverse('company_detail', kwargs={'pk': self.company.pk})

    def test_get_company_detail(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_company(self):
        updated_data = {'name': 'Samsung', 'phone': '0124578', 'email': "test@gmail.com",'address': 'New York'}
        response = self.client.put(self.url, updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.company.refresh_from_db()
        self.assertEqual(self.company.name, 'Samsung')

    def test_partial_update_company(self):
        partial_data = {'address': 'Dhaka'}
        response = self.client.patch(self.url, partial_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.company.refresh_from_db()
        self.assertEqual(self.company.address, 'Dhaka')

    def test_delete_company(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Company.objects.count(), 0)
