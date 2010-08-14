from django import forms
from django.db import models
from apps.pages.models import Page
from django.db.models import get_model
from apps.pages.widgets import WYMEditor

class ArticleAdminModelForm(forms.ModelForm):
    body = WYMEditor

    class Meta:
        model = Page
