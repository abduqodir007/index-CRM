from django import forms
from main.models import Users

class Add_UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    class Meta:
        model = Users
        fields = ['name', 'surname', 'gender', 'birth_date', 'phone_number', 'email', 'region', 'city_or_district', 'profile_image']
        widgets = {
            "name":forms.TextInput(attrs={"class": "form-control form-label ", "language": "all"}),
            "surname":forms.TextInput(attrs={"class": "form-control form-label"}),
            "gender":forms.TextInput(attrs={"class": "form-control form-label"}),
            "birth_date":forms.TextInput(attrs={"class": "form-control form-label"}),
            "phone_number":forms.TextInput(attrs={"class": "form-control form-label"}),
            "email":forms.TextInput(attrs={"class": "form-control form-label"}),
            "region":forms.TextInput(attrs={"class": "form-control form-label"}),
            "city_or_district":forms.TextInput(attrs={"class": "form-control form-label"}),
            'profile_image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }