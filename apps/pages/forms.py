from django import forms
from apps.pages.models import Page
from apps.pages.widgets import WYMEditor

class ArticleAdminModelForm(forms.ModelForm):
    body = WYMEditor

    class Meta:
        model = Page
