from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView, ListView
# from .forms import UserForm

from main import models



class HomeView(View):
    def get(self, request):

        return render(request, 'dashboard/index.html')
    

class Home2View(View):
    def get(self, request):
        
        return render(request, 'dashboard/index2.html')
    

class Home3View(View):
    def get(self, request):
        
        return render(request, 'dashboard/index3.html')
    

class Home4View(View):
    def get(self, request):
        
        return render(request, 'dashboard/index4.html')
    

class Home5View(View):
    def get(self, request):
        
        return render(request, 'dashboard/index5.html')
    
class Blog(View):
    def get(self, request):
        
        return render(request, 'dashboard/blog.html')

class AnalyticsView(View):
    def get(self, request):
        
        return render(request, 'dashboard/analytics.html')
    

class CrmView(View):
    def get(self, request):
        
        return render(request, 'crm.html')
    

class App_CalenderView(View):
    def get(self, request):
        
        return render(request, 'app-calender.html')
    

class App_Profile_1(View):
    def get(self, request):
        
        return render(request, 'app-profile-1.html')
    

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
        
        return render(request, 'chat.html')
    

    

class App_Profile_2(View):
    def get(self, request):
        
        return render(request, 'app-profile-2.html')
    

class Ecom_CheckoutView(View):
    def get(self, request):
        
        return render(request, 'ecom/ecom-checkout.html')
    


class Ecom_CustomersView(View):
    def get(self, request):
        
        return render(request, 'ecom/ecom-customers.html')
    

class Ecom_InvoiceView(View):
    def get(self, request):
        
        return render(request, 'ecom/ecom-invoice.html')
    

class Ecom_Product_DetailView(View):
    def get(self, request):
        
        return render(request, 'ecom/ecom-product-detail.html')
    

class Ecom_Product_GridView(View):
    def get(self, request):
        
        return render(request, 'ecom/ecom-product-grid.html')
    

class Ecom_Product_ListView(View):
    def get(self, request):
        
        return render(request, 'ecom/ecom-product-list.html')
    

class Ecom_Product_OrderView(View):
    def get(self, request):
        
        return render(request, 'ecom/ecom-product-order.html')
    

class Email_ComposeView(View):
    def get(self, request):
        
        return render(request, 'email/email-compose.html')
    

class Email_InboxView(View):
    def get(self, request):
        
        return render(request, 'email/email-inbox.html')
    

class Email_ReadView(View):
    def get(self, request):
        
        return render(request, 'email/email-read.html')
    

class Empty_PageView(View):
    def get(self, request):
        
        return render(request, 'email/empty-page.html')
    

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
    

class UserListView(ListView):
    queryset = models.Users.objects.all()
    template_name = 'apps/users-manager/user.html'
    context_object_name = "users"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context["users"] = models.Users.objects.all()

        return context

