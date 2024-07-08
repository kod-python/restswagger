from django.urls import path
from .views import ProductListCreateView, ProductRetrieveUpdateDestroyView
from django.conf import settings
from django.conf.urls.static import static
from .views import ProductImageUploadView



urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),
    path('products/<int:pk>/upload-image/', ProductImageUploadView.as_view(), name='product-image-upload'),
    # path('products/<int:pk>/upload', ImageUploadView.as_view(), name='image-upload'),
]   


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)