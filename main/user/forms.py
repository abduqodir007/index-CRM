from django import forms
from main.models import Users

class Add_UserForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Users
        fields = ['name', 'surname', 'gender', 'phone_number', 'birth_date', 'email', 'region', 'city_or_district', 'profile_image']
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ismingizni kiriting'}),
            'surname': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Familiyangizni kiriting'}),
            'gender': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Tanlash')] + list(Users.GENDER_CHOICES)),  # 'Tanlash' qo'shildi
            "email": forms.TextInput(attrs={"class": "form-control form-label",'placeholder': 'Email yozing'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefon raqamingiz'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'region': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Tanlash')] + list(Users.REGION_CHOICES)),  # 'Tanlash' qo'shildi
            'city_or_district': forms.Select(attrs={'class': 'form-control Select'}, choices=[('', 'Tanlash')] + list(Users.CITY_CHOICES)),  # 'Tanlash' qo'shildi
            'profile_image': forms.FileInput(attrs={'class': 'form-control', 'type': 'file'})
        }