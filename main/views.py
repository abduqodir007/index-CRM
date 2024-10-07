from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView, ListView
from main import models
from django.db.models import Q, Count




class HomeView(View):
    def get(self, request):

        return render(request, 'dashboard/index.html')
    

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
    


