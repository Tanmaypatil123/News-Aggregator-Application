from django import forms
from .models import News_data
class NewsForm(forms.ModelForm):
    class Meta:
        model: News_data
        fields = [
            "heading",
            "img",
            "url",
            "content",
        ]