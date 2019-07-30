from django import forms
from django.urls import reverse

from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'title'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Add Description'}))

    class Meta:
        model = Product
        fields = ['title', 'description', 'price']

    def get_absolute_url(self):
        return reverse("product-detail", kwargs={"id": self.id})

    # def clean_title(self):
    #     title = self.cleaned_data.get('title')
    #     if "CFE" not in self.cleaned_data.get('title'):
    #         raise forms.ValidationError("This is not a valid title")
    #     return title


class RawProductForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'title'}))
    description = forms.CharField(widget=forms.Textarea())
    price = forms.DecimalField()
