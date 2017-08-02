from django import forms
from django.contrib.auth.models import User
from .models import Dataset, DataInfo


class DatasetForm(forms.ModelForm):

    class Meta:
        model = Dataset
        fields = ['file_type', 'file_name', 'data_file']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class DataInfoForm(forms.ModelForm):

    class Meta:
        model = DataInfo
        fields = ['predict_fields', 'use_fields']


