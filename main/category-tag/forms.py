from django import forms
from main.models import ProductCategory, ProductTag



class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ['title', ]
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Kategoriya'})
            }
        
class ProductTagForm(forms.ModelForm):
    class Meta:
        model = ProductTag
        fields = ['title', ]
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Taglar'})
            }