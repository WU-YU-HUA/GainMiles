from django.urls import path, include
from storage import views

urlpatterns = [
    path('storage/<int:pk>/', views.StorageViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    })),
    path('size/<int:pk>/', views.SizeViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('color/<int:pk>/', views.ColorViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('storage/', views.StorageViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('size/', views.SizeViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('color/', views.ColorViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
]