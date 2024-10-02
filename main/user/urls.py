from django.urls import path

from .views import Add_UserDeleteView, Add_UserListView, Add_UserCreateView, Add_UserUdateView


urlpatterns = [
        path("", Add_UserListView.as_view(), name="add_user-list"),
        path("create/", Add_UserCreateView.as_view(), name="add_user-create"),
        path("<int:pk>/", Add_UserUdateView.as_view(), name="add_user-update"),
        path("delete/<int:pk>/", Add_UserDeleteView.as_view(), name="add_user-delete"),
        ]
