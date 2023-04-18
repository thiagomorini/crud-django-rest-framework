from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from backend.models import Module

class ModuleAPIViewTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = APIClient()
        cls.module_data = {
            'serial_number': '12345',
            'name': 'Test Module',
            'description': 'This is a description'
        }
        cls.module = Module.objects.create(**cls.module_data)

    def setUp(self):
        self.data = {
            'serial_number': '112233',
            'name': 'New Module',
            'description': 'This is a new description'
        }
        self.update_data = {
            'serial_number': '445566',
            'name': 'Updated Module',
            'description': 'This is an updated description'
        }

    def test_module_list(self):
        response = self.client.get(reverse('module_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, 'module_list.html')
        self.assertContains(response, self.module.serial_number)
        self.assertContains(response, self.module.name)
        self.assertContains(response, self.module.description)

    def test_module_create(self):
        response = self.client.post(reverse('module_create'), self.data)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertTrue(Module.objects.filter(serial_number=self.data['serial_number']).exists())

    def test_module_update(self):
        response = self.client.post(reverse('module_update', args=[self.module.pk]), self.update_data)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.module.refresh_from_db()
        self.assertEqual(self.module.serial_number, self.update_data['serial_number'])
        self.assertEqual(self.module.name, self.update_data['name'])
        self.assertEqual(self.module.description, self.update_data['description'])

    def test_module_delete(self):
        response = self.client.post(reverse('module_delete', args=[self.module.pk]))
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertFalse(Module.objects.filter(pk=self.module.pk).exists())

    def test_module_update_not_found(self):
        response = self.client.put(reverse('module_update', args=[999]), self.update_data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_module_delete_not_found(self):
        response = self.client.delete(reverse('module_delete', args=[999]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
