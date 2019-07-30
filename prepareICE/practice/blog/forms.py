from django import forms
from .models import Article


class ArticleModelForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'title'}))

    class Meta:
        model = Article
        fields = ['title', 'content', 'active']
