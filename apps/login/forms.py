from django import forms
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


no_space_validator = RegexValidator(r' ',_("No spaces allowed"), inverse_match=True,code='invalid_tag')

class FormLogin(forms.Form):
    username = forms.CharField(label="",validators= [no_space_validator],widget=forms.TextInput(attrs={'placeholder': 'Username or Email', 'style': 'width: 300px;', 'class': 'form-control'}), required=True)
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'style': 'width: 300px;', 'class': 'form-control'}), required=True)

class CreateAccountForm(forms.Form):
    first_name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}), required=True)
    last_name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Last Name','class': 'form-control'}), required=True)
    email = forms.EmailField(label="", widget=forms.EmailInput(attrs={'placeholder': 'Email','class': 'form-control'}), required=True)
    new_username = forms.CharField(label="",validators=[no_space_validator] ,widget=forms.TextInput(attrs={'placeholder': 'Username','class': 'form-control'}), required=True)
    new_password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'Password','class': 'form-control'}), required=True)
    confirm_password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password','class': 'form-control'}), required=True)

class DateInput(forms.DateInput):
    input_type = "date"

class AddTaskForm(forms.Form):
    new_task = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'New Task', 'style': 'width: 300px;', 'class': 'form-control'}), required=True)
    finish_by = forms.DateTimeField(label="", widget=DateInput(attrs={'placeholder': 'Finish By', 'style': 'width: 300px;', 'class': 'form-control'}), required=True)