from django.urls import path
from .views import ModuleListView, ModuleCreateView, ModuleUpdateView, ModuleDeleteView

urlpatterns = [
    path('modules/', ModuleListView.as_view(), name='module_list'),
    path('modules/create/', ModuleCreateView.as_view(), name='module_create'),
    path('modules/<int:pk>/', ModuleUpdateView.as_view(), name='module_update'),
    path('modules/<int:pk>/delete/', ModuleDeleteView.as_view(), name='module_delete'),
]
