from os import name
from django import forms
from django.db.models import fields
from django.forms import widgets
from django.forms.widgets import Widget
from .models import *


class ApplyForms(forms.ModelForm):
    class Meta:
        model=StudentApply
        fields="__all__"

        widgets={
            'name':forms.TextInput(attrs={'class':'wp-form-control wpcf7-text', 'type':'text', 'name':'name', 'placeholder':'Adınız', 'style':'width: 48%; float: left;'}),
            'surname':forms.TextInput(attrs={'class':'wp-form-control wpcf7-text', 'type':'text', 'name':'surname', 'placeholder':'Soyadınız', 'style':'width: 48%; float: right;'}),
            'country':forms.Select(attrs={'class':'wp-form-control wpcf7-text', 'name':'country', 'style':'color: #666;', 'aria-required':'true', 'aira-invalid':'true'}),
            'born_date':forms.DateInput(attrs={'class':'wp-form-control wpcf7-text', 'type':'date', 'name':'born_date', 'placeholder':'Doğum Tarihiniz', 'style':'width: 48%; float: left; color: #666;'}),
            'gender': forms.Select(attrs={'class':'wp-form-control wpcf7-text', 'name':'gender',  'placeholder':'Cinsiyyetiniz' , 'style':'width: 48%; float: right; color: #666;'}),
            'phone':forms.NumberInput(attrs={'class':'wp-form-control wpcf7-text', 'type':'number', 'name':'phone', 'placeholder':'Telefon Numaranız'}),
            'email': forms.EmailInput(attrs={'class':'wp-form-control wpcf7-text', 'type':'email','placeholder':'Email Adresiniz'}),
            'university':forms.Select(attrs={'class':'wp-form-control wpcf7-text', 'name':'uni', 'placeholder': 'İstediğiniz Üniversite' , 'style':'width: 48%; float: left; color: #666;', }),
            'program': forms.TextInput(attrs={'class':'wp-form-control wpcf7-text', 'type':'text', 'name':'program', 'placeholder':'İstediğiniz Program', 'style':'width: 48%; float: right;'}),
            'edu_degree':forms.Select(attrs={'class':'wp-form-control wpcf7-text', 'name':'degree', 'style':'width: 48%; float: left; color: #666;', }),
            'edu_lang': forms.Select(attrs={'class':'wp-form-control wpcf7-text', 'name':'lang', 'style':'width: 48%; float: right; color: #666;'}),
            'budget':forms.NumberInput(attrs={'class':'wp-form-control wpcf7-text', 'type':'number'  ,'name':'budget' ,'placeholder':'Bütçeniz', 'style':'width: 48%; float: left;' }),
            'edu_currency':forms.Select(attrs={'class':'wp-form-control wpcf7-text', 'name':'currency', 'style':'width: 48%; float: right; color: #666;'}),
            'diploma': forms.FileInput(attrs={'class':'wp-form-control wpcf7-text','type':'file', 'name':'diploma'}),
            'note':forms.FileInput(attrs={'class':'wp-form-control wpcf7-text','type':'file', 'name':'note'}),
            'passport':forms.FileInput(attrs={'class':'wp-form-control wpcf7-text','type':'file', 'name':'passport'}),
            'photo':forms.FileInput(attrs={'class':'wp-form-control wpcf7-text','type':'file', 'name':'passport'}),
            'message': forms.Textarea(attrs={'class':'wp-form-control wpcf7-text', 'name':'message', 'rows':'10', 'cols':'30'})

        }    