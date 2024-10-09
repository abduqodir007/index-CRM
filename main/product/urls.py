from django.urls import path

from .views import ProductDeleteView, ProductListView, ProductCreateView, ProductUpdateView, OrderListView, ProductSaleView

urlpatterns = [
        path("", ProductListView.as_view(), name="product-list"),
        path("create/", ProductCreateView.as_view(), name="product-create"),
        path("update/<int:pk>/", ProductUpdateView.as_view(), name="product-update"),
        path("delete/<int:pk>/", ProductDeleteView.as_view(), name="product-delete"),

        path('product-sale/<int:pk>/', ProductSaleView.as_view(), name='product-sale'),
        path('order-list/', OrderListView.as_view(), name='order-list'),
        ]
