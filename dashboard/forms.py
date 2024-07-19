from django import forms
from products.models import *


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'subcategory', 'title', 'description', 'image', 'brand', 'colors', 'price', 'countInStock']
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ['name', 'color', 'image']