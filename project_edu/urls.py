from django.urls import path, include

urlpatterns = [
    path('api/', include('backend.urls')),
    path('', include('frontend.urls')),
]
