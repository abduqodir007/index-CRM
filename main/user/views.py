from django.views.generic import ListView

from main.models import Users
from helpers.views import CreateView, UpdateView, DeleteView

from .forms import Add_UserForm

class Add_UserListView(ListView):
    model = Users
    template_name = "apps/users-manager/user.html"
    context_object_name = "users"
    queryset = model.objects.all().order_by("-id")
    paginate_by = 10

    def get_queryset(self):
        object_list = self.queryset
        search = self.request.GET.get("search", None)
        if search:
            object_list = object_list.filter(name__icontains=search)

        return object_list


class Add_UserCreateView(CreateView):
    model = Users
    form_class = Add_UserForm
    template_name = "apps/users-manager/add-admin.html"
    context_object_name = "object"
    success_url = "main:add_user-list"
    success_create_url = "main:add_user-create"
    
    
class Add_UserUdateView(UpdateView):
    model = Users
    template_name = "apps/users-manager/edit-admin.html"
    form_class = Add_UserForm
    context_object_name = "object"
    success_url = "main:add_user-list"
    success_create_url = "main:add_user-update"


class Add_UserDeleteView(DeleteView):
    model = Users
    success_url = "main:add_user-list"

