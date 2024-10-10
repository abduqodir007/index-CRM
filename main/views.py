from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView, ListView, TemplateView
from main import models
from django.db.models import Q, Count, Sum
from django.utils import timezone
from datetime import timedelta
from main.models import Product, Order


class DashboardView(TemplateView):
    template_name = 'dashboard/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = timezone.now().date()
        week_start = today - timedelta(days=today.weekday())
        month_start = today.replace(day=1)
        year_start = today.replace(month=1, day=1)

        # Productlar bo'yicha hisoblash
        context['daily_products'] = Product.objects.filter(created_at__date=today).count()
        context['weekly_products'] = Product.objects.filter(created_at__date__gte=week_start).count()
        context['monthly_products'] = Product.objects.filter(created_at__date__gte=month_start).count()
        context['yearly_products'] = Product.objects.filter(created_at__date__gte=year_start).count()

        # Sotilgan productlar va ularning foydasini hisoblash
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

from django.http import JsonResponse
from django.utils import timezone
from datetime import timedelta

def get_statistics(request):
    today = timezone.now().date()
    week_start = today - timedelta(days=today.weekday())
    month_start = today.replace(day=1)
    year_start = today.replace(month=1, day=1)

    # Statistika ma'lumotlari
    stats_type = request.GET.get('type')
    data = {}

    if stats_type == 'week':
        weekly_sales = Order.objects.filter(sale_date__date__gte=week_start)
        data['sales'] = weekly_sales.aggregate(Sum('total_price'))['total_price__sum'] or 0
        data['sold_count'] = weekly_sales.aggregate(Sum('sale_count'))['sale_count__sum'] or 0
    elif stats_type == 'month':
        monthly_sales = Order.objects.filter(sale_date__date__gte=month_start)
        data['sales'] = monthly_sales.aggregate(Sum('total_price'))['total_price__sum'] or 0
        data['sold_count'] = monthly_sales.aggregate(Sum('sale_count'))['sale_count__sum'] or 0
    elif stats_type == 'year':
        yearly_sales = Order.objects.filter(sale_date__date__gte=year_start)
        data['sales'] = yearly_sales.aggregate(Sum('total_price'))['total_price__sum'] or 0
        data['sold_count'] = yearly_sales.aggregate(Sum('sale_count'))['sale_count__sum'] or 0
    else:
        # Kunlik statistika
        daily_sales = Order.objects.filter(sale_date__date=today)
        data['sales'] = daily_sales.aggregate(Sum('total_price'))['total_price__sum'] or 0
        data['sold_count'] = daily_sales.aggregate(Sum('sale_count'))['sale_count__sum'] or 0

    return JsonResponse(data)



class Home2View(View):
    def get(self, request):
        
        return render(request, 'dashboard/index-2.html')
    

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
    