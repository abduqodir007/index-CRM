from django.urls import path

from main import views

app_name = "main"


urlpatterns = [
        path("", views.HomeView.as_view(), name="home"),
        path("home2/", views.Home2View(), name="home2"),
        path("home3/", views.Home2View(), name="home3"),
        path("home4/", views.Home2View(), name="home4"),
        path("home5/", views.Home2View(), name="home5"),
        path("analytics/", views.AnalyticsView(), name="analytics"),
        path("app-calender/", views.App_CalenderView(), name="app-calender"),
        path("app-profile1/", views.App_Profile_1(), name="app-profile1"),
        path("app-profile2/", views.App_Profile_2(), name="app-profile2"),
        path("blog/", views.Blog(), name="blog"),
        path("chart-chartist/", views.Chart_chartist(), name="chart-chartist"),
        path("chart-chartjs/", views.Chart_chartjs(), name="chart-chartjs"),
        path("chart-flot/", views.Chart_flot(), name="chart-flot"),
        path("chart-morris/", views.Chart_morris(), name="chart-morris"),
        path("chart-peity/", views.Chart_peity(), name="chart-peity"),
        path("chart-sparkline/", views.Chart_sparkline(), name="chart-sparkline"),
        path("crm/", views.CrmView(), name="crm"),
        path("ecom-checkout/", views.Ecom_CheckoutView(), name="ecom-checkout"),
        path("ecom-custumers/", views.Ecom_CustomersView(), name="ecom-customers"),
        path("ecom-invoice/", views.Ecom_InvoiceView(), name="ecom-invoice"),
        path("ecom-product-detail/", views.Ecom_Product_DetailView(), name="ecom-product-detail"),
        path("ecom-product-grid/", views.Ecom_Product_GridView(), name="ecom-product-grid"),
        path("ecom-product-list/", views.Ecom_Product_ListView(), name="ecom-product-list"),
        path("ecom-product-order/", views.Ecom_Product_OrderView(), name="ecom-product-order"),
        path("edit-profile/", views.Edit_ProfileView(), name="edit-profile"),
        path("email-compose/", views.Email_ComposeView(), name="email-compose"),
        path("email-inbox/", views.Email_InboxView(), name="email-inbox"),
        path("email-read/", views.Email_ReadView(), name="email-read"),
        path("empty-page/", views.Empty_PageView(), name="empty-page"),
        path("form-ckeditor/", views.Form_CkeditorView(), name="form-ckeditpr"),
        path("form-element/", views.Form_ElementView(), name="form-element"),
        path("form-pickers/", views.Form_PickersView(), name="form-pickers"),
        path("form-validation/", views.Form_ValidationView(), name="form-validation"),
        path("form-wizard/", views.Form_WizardView(), name="form-wizard"),

]