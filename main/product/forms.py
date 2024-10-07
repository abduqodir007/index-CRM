from django import forms
from main.models import Product

class ProductForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Product
        fields = ['title', 'product_code', 'categories', 'tags', 'main_image', 'main_image1', 'main_image2', 'main_image3', 'price', 'brand', 'product_count', 'is_top', 'description']
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Mahsulot nomini kiriting'}),
            'categories': forms.SelectMultiple(attrs={'class': 'custom-select form-control col-lg-12 col-md-12 col-sm-12'}),
            'tags': forms.SelectMultiple(attrs={'class': 'custom-select form-control col-lg-12 col-md-12 col-sm-12'}),
            "price": forms.TextInput(attrs={"class": "form-control form-label",'placeholder': 'Mahsulot Narxini yozing'}),
            "brand": forms.TextInput(attrs={"class": "form-control form-label",'placeholder': 'Mahsulot Brandi yozing'}),
            'product_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mahsulot Shetirif kodi'}),
            'main_image': forms.FileInput(attrs={'class': 'form-control', 'type': 'file'}),
            'main_image1': forms.FileInput(attrs={'class': 'form-control', 'type': 'file'}),
            'main_image2': forms.FileInput(attrs={'class': 'form-control', 'type': 'file'}),
            'main_image3': forms.FileInput(attrs={'class': 'form-control', 'type': 'file'}),
            'is_top': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
            'product_count': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Mahsulot Haqida Malumot kiriting'}),
        }
