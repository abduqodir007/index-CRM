from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView, ListView, TemplateView
from main import models
from django.db.models import Q, Count, Sum
from django.utils import timezone
from datetime import timedelta
from main.models import Product, Order
from django.http import JsonResponse
from django.utils.safestring import mark_safe
import json
from decimal import Decimal

# class DashboardView(TemplateView):
#     template_name = 'dashboard/index.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
        
#         today = timezone.now().date()
#         week_start = today - timedelta(days=today.weekday())
#         year_start = today.replace(month=1, day=1)

#         # Oylik sotuvlar statistikasi
#         monthly_sales_data = []
#         monthly_revenue_data = []
#         monthly_order_counts = []

#         for month in range(1, 13):
#             sales_in_month = Order.objects.filter(sale_date__month=month).aggregate(total_sales=Sum('sale_count'))['total_sales'] or 0
#             revenue_in_month = Order.objects.filter(sale_date__month=month).aggregate(total_revenue=Sum('total_price'))['total_revenue'] or Decimal(0)
#             orders_in_month = Order.objects.filter(sale_date__month=month).count()

#             monthly_sales_data.append(sales_in_month)
#             monthly_revenue_data.append(float(revenue_in_month))
#             monthly_order_counts.append(orders_in_month)

#         # Haftalik sotuvlar statistikasi
#         weekly_sales_data = []
#         weekly_revenue_data = []
#         weekly_order_counts = []

#         for i in range(0, 7):
#             day = week_start + timedelta(days=i)
#             sales_in_day = Order.objects.filter(sale_date__date=day).aggregate(total_sales=Sum('sale_count'))['total_sales'] or 0
#             revenue_in_day = Order.objects.filter(sale_date__date=day).aggregate(total_revenue=Sum('total_price'))['total_revenue'] or Decimal(0)
#             orders_in_day = Order.objects.filter(sale_date__date=day).count()

#             weekly_sales_data.append(sales_in_day)
#             weekly_revenue_data.append(float(revenue_in_day))
#             weekly_order_counts.append(orders_in_day)

#         # Yillik sotuvlar statistikasi
#         yearly_sales_data = []
#         yearly_revenue_data = []
#         yearly_order_counts = []

#         for month in range(1, 13):
#             sales_in_month = Order.objects.filter(sale_date__month=month, sale_date__year=today.year).aggregate(total_sales=Sum('sale_count'))['total_sales'] or 0
#             revenue_in_month = Order.objects.filter(sale_date__month=month, sale_date__year=today.year).aggregate(total_revenue=Sum('total_price'))['total_revenue'] or Decimal(0)
#             orders_in_month = Order.objects.filter(sale_date__month=month, sale_date__year=today.year).count()

#             yearly_sales_data.append(sales_in_month)
#             yearly_revenue_data.append(float(revenue_in_month))
#             yearly_order_counts.append(orders_in_month)

#         # Kontekstga qo'shish
#         context['monthly_sales_data'] = monthly_sales_data
#         context['monthly_revenue_data'] = monthly_revenue_data
#         context['monthly_order_counts'] = monthly_order_counts

#         context['weekly_sales_data'] = weekly_sales_data
#         context['weekly_revenue_data'] = weekly_revenue_data
#         context['weekly_order_counts'] = weekly_order_counts

#         context['yearly_sales_data'] = yearly_sales_data
#         context['yearly_revenue_data'] = yearly_revenue_data
#         context['yearly_order_counts'] = yearly_order_counts

#         return context


class DashboardView(TemplateView):
    template_name = 'dashboard/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = timezone.now().date()
        week_start = today - timedelta(days=today.weekday())
        month_start = today.replace(day=1)
        year_start = today.replace(month=1, day=1)

        context['daily_products'] = Product.objects.filter(created_at__date=today).count()
        context['weekly_products'] = Product.objects.filter(created_at__date__gte=week_start).count()
        context['monthly_products'] = Product.objects.filter(created_at__date__gte=month_start).count()
        context['yearly_products'] = Product.objects.filter(created_at__date__gte=year_start).count()

        daily_sales = Order.objects.filter(sale_date__date=today)
        context['daily_sales'] = daily_sales.aggregate(Sum('total_price'))['total_price__sum'] or 0
        context['daily_sold_count'] = daily_sales.aggregate(Sum('sale_count'))['sale_count__sum'] or 0        
        context['daily_profit'] = sum(
            (sale.product.price - sale.product.cost_price) * sale.sale_count for sale in daily_sales
        )

        weekly_sales = Order.objects.filter(sale_date__date__gte=week_start)
        context['weekly_sales'] = weekly_sales.aggregate(Sum('total_price'))['total_price__sum'] or 0
        context['weekly_sold_count'] = weekly_sales.aggregate(Sum('sale_count'))['sale_count__sum'] or 0
        
        context['weekly_profit'] = sum(
            (sale.product.price - sale.product.cost_price) * sale.sale_count for sale in weekly_sales
        )

        monthly_sales = Order.objects.filter(sale_date__date__gte=month_start)
        context['monthly_sales'] = monthly_sales.aggregate(Sum('total_price'))['total_price__sum'] or 0
        context['monthly_sold_count'] = monthly_sales.aggregate(Sum('sale_count'))['sale_count__sum'] or 0
        
        context['monthly_profit'] = sum(
            (sale.product.price - sale.product.cost_price) * sale.sale_count for sale in monthly_sales
        )

        yearly_sales = Order.objects.filter(sale_date__date__gte=year_start)
        context['yearly_sales'] = yearly_sales.aggregate(Sum('total_price'))['total_price__sum'] or 0
        context['yearly_sold_count'] = yearly_sales.aggregate(Sum('sale_count'))['sale_count__sum'] or 0       
        context['yearly_profit'] = sum(
            (sale.product.price - sale.product.cost_price) * sale.sale_count for sale in yearly_sales
        )

        context['total_revenue'] = Order.objects.aggregate(Sum('total_price'))['total_price__sum'] or 0
        context['total_spent'] = Order.objects.aggregate(Sum('total_price'))['total_price__sum'] or 0
        context['total_sold_count'] = Order.objects.aggregate(Sum('sale_count'))['sale_count__sum'] or 0
        context['remaining_products'] = Product.objects.aggregate(Sum('product_count'))['product_count__sum'] or 0

        return context

class Home3View(View):
    def get(self, request):
        
        return render(request, 'dashboard/index-3.html')
    

class Home4View(View):
    def get(self, request):
        
        return render(request, 'dashboard/index-4.html')
    

class Home5View(View):
    def get(self, request):
        
        return render(request, 'dashboard/index-5.html')
    
class Blog(View):
    def get(self, request):
        
        return render(request, 'dashboard/blog.html')

class AnalyticsView(View):
    def get(self, request):
        
        return render(request, 'dashboard/analytics.html')
    

class CrmView(View):
    def get(self, request):
        
        return render(request, 'dashboard/crm.html')
    

# class ProductsView(View):
#     def get(self, request):
        
#         return render(request, 'dashboard/products.html')
    

class SalesView(View):
    def get(self, request):
        
        return render(request, 'dashboard/sales.html')


class App_CalendarView(View):
    def get(self, request):
        
        return render(request, 'apps/app-calender.html')
    

class App_Profile_1(View):
    def get(self, request):
        
        return render(request, 'apps/users-manager/app-profile-1.html')
    

class App_Profile_2(View):
    def get(self, request):
        
        return render(request, 'apps/users-manager/app-profile-2.html')
    

class Chart_chartist(View):
    def get(self, request):
        
        return render(request, 'charts/chart-chartist.html')
    

class Chart_chartjs(View):
    def get(self, request):
        
        return render(request, 'charts/chart-chartjs.html')
        

class Chart_flot(View):
    def get(self, request):
        
        return render(request, 'charts/chart-flot.html')


class Chart_morris(View):
    def get(self, request):
        
        return render(request, 'charts/chart-morris.html')
    

class Chart_peity(View):
    def get(self, request):
        
        return render(request, 'charts/chart-peity.html')
    

class Chart_sparkline(View):
    def get(self, request):
        
        return render(request, 'charts/chart-sparkline.html')
    

class Chatview(View):
    def get(self, request):
        
        return render(request, 'pages/chat.html')
    

class Ecom_CheckoutView(View):
    def get(self, request):
        
        return render(request, 'apps/shop/ecom-checkout.html')
    


class Ecom_CustomersView(View):
    def get(self, request):
        
        return render(request, 'apps/shop/ecom-customers.html')
    

class Ecom_InvoiceView(View):
    def get(self, request):
        
        return render(request, 'apps/shop/ecom-invoice.html')
    
    
class Ecom_Product_DetailView(DetailView):
    queryset = models.Product.objects.all()
    slug_field = "slug"
    context_object_name = "object"
    template_name = 'apps/shop/product/ecom-product-detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["related_products"] = models.Product.objects.filter(
                ~Q(slug=self.kwargs["slug"]), categories__in=self.get_object().categories.all()
                )[:4]

        return context

    
class Ecom_Product_GridView(View):
    def get(self, request):
        
        return render(request, 'apps/shop/ecom-product-grid.html')


class Email_ComposeView(View):
    def get(self, request):
        
        return render(request, 'apps/email/email-compose.html')
    

class Email_InboxView(View):
    def get(self, request):
        
        return render(request, 'apps/email/email-inbox.html')
    

class Email_ReadView(View):
    def get(self, request):
        
        return render(request, 'apps/email/email-read.html')
    

class Empty_PageView(View):
    def get(self, request):
        
        return render(request, 'pages/empty-page.html')
    

class Form_CkeditorView(View):
    def get(self, request):
        
        return render(request, 'forms/form-ckeditor.html')
    

class Form_ElementView(View):
    def get(self, request):
        
        return render(request, 'forms/form-element.html')
    

class Form_PickersView(View):
    def get(self, request):
        
        return render(request, 'forms/form-pickers.html')
    

class Form_ValidationView(View):
    def get(self, request):
        
        return render(request, 'forms/form-validation.html')
    

class Form_WizardView(View):
    def get(self, request):
        
        return render(request, 'forms/form-wizard.html')
    