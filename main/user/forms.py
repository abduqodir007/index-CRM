from django import forms
from main.models import Users

class Add_UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['name', 'surname', 'gender', 'birth_date', 'phone_number', 'email', 'region', 'city_or_district', 'profile_image']