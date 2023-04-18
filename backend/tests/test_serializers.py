from django.test import TestCase
from backend.models import Module
from backend.serializers import ModuleSerializer

class ModuleSerializerTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Module.objects.create(
            serial_number='12345',
            name='Test Module',
            description='This is a description'
        )

    def setUp(self):
        self.module = Module.objects.get(id=1)
        self.serializer_data = ModuleSerializer(instance=self.module).data

    def test_module_serializer_fields(self):
        self.assertEqual(
            set(self.serializer_data.keys()),
            set(['id', 'serial_number', 'name', 'description'])
        )

    def test_module_deserializer_valid_data(self):
        serializer = ModuleSerializer(data=self.serializer_data)
        self.assertTrue(serializer.is_valid())
        module = serializer.save()
        self.assertIsInstance(module, Module)
