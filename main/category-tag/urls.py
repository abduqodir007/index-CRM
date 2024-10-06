from django.urls import path

from .views import ProductCategoryCreateView, ProductTagCreateView


urlpatterns = [
        path('create/', ProductCategoryCreateView.as_view(), name='category-create'),
        path('tagcreate/', ProductTagCreateView.as_view(), name='tag-create'),
        ]
