from django.contrib.auth.models import User
from django import forms
from .models import *

class public_complaints_form(forms.ModelForm):

    class Meta():
        model = public_complaints
        fields = '__all__'
        #fields = ['complaint', 'complaint_type', 'complaint_name', 'description', 'complaint_photo']
