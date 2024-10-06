from django.urls import path

from .views import ProductDeleteView, ProductListView, ProductCreateView, ProductUpdateView
from .import views

urlpatterns = [
        path("", ProductListView.as_view(), name="product-list"),
        path("create/", ProductCreateView.as_view(), name="product-create"),
        path("update/<int:pk>/", ProductUpdateView.as_view(), name="product-update"),
        path("delete/<int:pk>/", ProductDeleteView.as_view(), name="product-delete"),

        path('product-sale/<int:pk>/', views.product_sale, name='product-sale'),
        ]
