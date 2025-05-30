from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Notice

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    department = forms.ChoiceField(choices=Notice.DEPARTMENT_CHOICES, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'department', 'password1', 'password2']

class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ['title', 'content', 'department', 'notice_type', 'is_important', 'valid_until']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'notice_type': forms.Select(attrs={'class': 'form-control'}),
            'is_important': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'valid_until': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class NoticeSearchForm(forms.Form):
    search = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Search notices...'
    }))
    department = forms.ChoiceField(required=False, widget=forms.Select(attrs={
        'class': 'form-control'
    }))
    notice_type = forms.ChoiceField(required=False, widget=forms.Select(attrs={
        'class': 'form-control'
    }))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['department'].choices = [('', 'All Departments')] + list(Notice.DEPARTMENT_CHOICES)
        self.fields['notice_type'].choices = [('', 'All Types')] + list(Notice.NOTICE_TYPE_CHOICES) 