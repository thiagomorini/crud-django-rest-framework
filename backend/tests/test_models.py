from django.test import TestCase
from backend.models import Module

class ModuleModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Module.objects.create(
            serial_number='12345',
            name='Test Module',
            description='This is a description'
        )

    def setUp(self):
        self.module = Module.objects.get(id=1)

    def test_module_serial_number_max_length(self):
        max_length = self.module._meta.get_field('serial_number').max_length
        self.assertEquals(max_length, 20)

    def test_module_name_max_length(self):
        max_length = self.module._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)

    def test_module_serial_number(self):
        self.assertEqual(self.module.serial_number, "12345")

    def test_module_name(self):
        self.assertEqual(self.module.name, "Test Module")

    def test_module_description(self):
        self.assertEqual(self.module.description, "This is a description")

    def test_module_str(self):
        self.assertEqual(
            str(self.module),
            "Serial Number: 12345 Name: Test Module"
        )
