from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from rest_framework.exceptions import NotFound
from django.http import Http404
from .models import Module
from .serializers import ModuleSerializer

class ModuleListAPIView(ListAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

class ModuleCreateAPIView(CreateAPIView):
    serializer_class = ModuleSerializer

class ModuleUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

    def get_object(self):
        try:
            return super().get_object()
        except NotFound:
            raise Http404("Module does not exist")

class ModuleDeleteAPIView(RetrieveDestroyAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

    def get_object(self):
        try:
            return super().get_object()
        except NotFound:
            raise Http404("Module does not exist")
