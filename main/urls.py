from django.urls import path, include

from main import views

app_name = "main"


urlpatterns = [
        path("", views.HomeView.as_view(), name="home"),
        path("home2/", views.Home2View.as_view(), name="home2"),
        path("home3/", views.Home3View.as_view(), name="home3"),
        path("home4/", views.Home4View.as_view(), name="home4"),
        path("home5/", views.Home5View.as_view(), name="home5"),
        path("analytics/", views.AnalyticsView.as_view(), name="analytics"),
        path("app-calender/", views.App_CalenderView.as_view(), name="app-calender"),
        path("app-profile1/", views.App_Profile_1.as_view(), name="app-profile1"),
        path("app-profile2/", views.App_Profile_2.as_view(), name="app-profile2"),
        path("blog/", views.Blog.as_view(), name="blog"),
        path("chart-chartist/", views.Chart_chartist.as_view(), name="chart-chartist"),
        path("chart-chartjs/", views.Chart_chartjs.as_view(), name="chart-chartjs"),
        path("chart-flot/", views.Chart_flot.as_view(), name="chart-flot"),
        path("chart-morris/", views.Chart_morris.as_view(), name="chart-morris"),
        path("chart-peity/", views.Chart_peity.as_view(), name="chart-peity"),
        path("chart-sparkline/", views.Chart_sparkline.as_view(), name="chart-sparkline"),
        path("crm/", views.CrmView.as_view(), name="crm"),
        path("ecom-checkout/", views.Ecom_CheckoutView.as_view(), name="ecom-checkout"),
        path("ecom-custumers/", views.Ecom_CustomersView.as_view(), name="ecom-customers"),
        path("ecom-invoice/", views.Ecom_InvoiceView.as_view(), name="ecom-invoice"),
        path("ecom-product-detail/", views.Ecom_Product_DetailView.as_view(), name="ecom-product-detail"),
        path("ecom-product-grid/", views.Ecom_Product_GridView.as_view(), name="ecom-product-grid"),
        path("ecom-product-list/", views.Ecom_Product_ListView.as_view(), name="ecom-product-list"),
        path("ecom-product-order/", views.Ecom_Product_OrderView.as_view(), name="ecom-product-order"),
        path("email-compose/", views.Email_ComposeView.as_view(), name="email-compose"),
        path("email-inbox/", views.Email_InboxView.as_view(), name="email-inbox"),
        path("email-read/", views.Email_ReadView.as_view(), name="email-read"),
        path("empty-page/", views.Empty_PageView.as_view(), name="empty-page"),
        path("form-ckeditor/", views.Form_CkeditorView.as_view(), name="form-ckeditpr"),
        path("form-element/", views.Form_ElementView.as_view(), name="form-element"),
        path("form-pickers/", views.Form_PickersView.as_view(), name="form-pickers"),
        path("form-validation/", views.Form_ValidationView.as_view(), name="form-validation"),
        path("form-wizard/", views.Form_WizardView.as_view(), name="form-wizard"),

        path("users/", include("main.user.urls")),
]