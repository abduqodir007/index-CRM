from django.views.generic import CreateView
from main.models import ProductCategory, ProductTag
from helpers.views import DeleteView
from django.urls import reverse_lazy

from .forms import ProductCategoryForm, ProductTagForm


class ProductCategoryCreateView(CreateView):
    model = ProductCategory
    form_class = ProductCategoryForm
    template_name = "apps/shop/category-tag/product-category.html"
    context_object_name = "object"
    success_url = reverse_lazy("main:product-create")

                
class ProductCategoryDeleteView(DeleteView):
    model = ProductCategory
    success_url = reverse_lazy("main:product-create")


class ProductTagCreateView(CreateView):
    model = ProductTag
    form_class = ProductTagForm
    template_name = "apps/shop/category-tag/product-tag.html"
    context_object_name = "object"
    success_url = reverse_lazy("main:product-create")

                
class ProductDeleteView(DeleteView):
    model = ProductTag
    success_url = reverse_lazy("main:product-create")
