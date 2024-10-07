from django.views.generic import ListView, CreateView, UpdateView
from helpers.views import  DeleteView

from django.shortcuts import redirect, get_object_or_404
from main.models import Product
from django.urls import reverse_lazy, reverse
from .forms import ProductForm

class ProductListView(ListView):
    model = Product
    template_name = "apps/shop/product/ecom-product-list.html"
    context_object_name = "objects"
    queryset = model.objects.all().order_by("-id")
    paginate_by = 10
    
    def get_queryset(self):
        object_list = self.queryset
        search = self.request.GET.get("search", None)
        if search:
            object_list = object_list.filter(title__icontains=search)

        return object_list

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "apps/shop/product/add-product.html"
    context_object_name = "object"
    success_url = reverse_lazy("main:product-list")


                
class ProductUpdateView(UpdateView):
    model = Product
    template_name = "apps/shop/product/update-product.html"
    form_class = ProductForm
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    
    def get_success_url(self):
        return reverse_lazy('main:product-update', kwargs={'slug': self.object.slug})

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'main/product_confirm_delete.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('product-list')


def product_sale(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if product.product_count > 0:
        product.product_count -= 1
        product.save()

    return redirect(reverse('main:product-list'))

