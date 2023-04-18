from django.urls import path
from .views import ModuleListAPIView, ModuleCreateAPIView, ModuleUpdateAPIView, ModuleDeleteAPIView

urlpatterns = [
    path('modules/', ModuleListAPIView.as_view(), name='module_list'),
    path('modules/create/', ModuleCreateAPIView.as_view(), name='module_create'),
    path('modules/<int:pk>/', ModuleUpdateAPIView.as_view(), name='module_update'),
    path('modules/<int:pk>/delete/', ModuleDeleteAPIView.as_view(), name='module_delete'),
]
