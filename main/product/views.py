from django.views.generic import ListView, CreateView, UpdateView
from datetime import timedelta
from django.views import View
from helpers.views import DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from main.models import Product, Order
from django.urls import reverse_lazy, reverse
from .forms import ProductForm
from django.utils.text import slugify
from django.contrib import messages
from django.utils import timezone
from django.db.models import Sum, Count


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
    form_class = ProductForm
    template_name = "apps/shop/product/update-product.html"
    context_object_name = "object"
    success_url = reverse_lazy("main:product-list") 

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)
                       

class ProductDeleteView(DeleteView):
    model = Product
    success_url = "main:product-list"


class ProductSaleView(View):
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        
        try:
            sale_count = int(request.POST.get('num', 1))
        except ValueError:
            sale_count = 1

        if sale_count <= 0:
            return render(request, 'pages/error.page-error-400.html', {'error': 'Mahsulot miqdori manfiy yoki nol bo\'lmasligi kerak'})

        if product.product_count >= sale_count:
            product.product_count -= sale_count
            product.save()

            total_price = product.price * sale_count
            Order.objects.create(
                product=product,
                sale_count=sale_count,
                total_price=total_price,
                sale_date=timezone.now()
            )

            messages.success(request, f"{sale_count} dona {product.title} sotildi. Umumiy narx: {total_price} so'm")
        else:
            return render(request, 'pages/error.page-error-400.html', {'error': 'Stokda yetarli mahsulot mavjud emas'})

        return redirect(reverse('main:product-list'))

class OrderListView(ListView):
    model = Order
    template_name = 'apps/shop/product/product-order.html'
    context_object_name = 'orders'
    ordering = ['-sale_date']
    