from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *
from .models import Admin
from django.contrib.auth import authenticate



class CreateUserForm(UserCreationForm):
	class Meta:
	  model = User
	  fields = ['first_name','last_name','username', 'email', 'password1', 'password2']

# class RegistrationForm(UserCreationForm):
#     """
#       Form for Registering new users 
#     """
#     email = forms.EmailField(max_length=60, help_text = 'Required. Add a valid email address')
#     class Meta:
#         model = Admin
#         fields = ('email', 'username', 'password1', 'password2')

#     def __init__(self, *args, **kwargs):
#         """
#           specifying styles to fields 
#         """
#         super(RegistrationForm, self).__init__(*args, **kwargs)
#         for field in (self.fields['email'],self.fields['username'],self.fields['password1'],self.fields['password2']):
#             field.widget.attrs.update({'class': 'form-control '})


class AccountAuthenticationForm(forms.ModelForm):
    """
      Form for Logging in  users
    """
    password  = forms.CharField(label= 'Password', widget=forms.PasswordInput)

    class Meta:
        model  =  Admin
        fields =  ('email', 'password')
        widgets = {
                   'email':forms.TextInput(attrs={'class':'form-control'}),
                   'password':forms.TextInput(attrs={'class':'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        """
          specifying styles to fields 
        """
        super(AccountAuthenticationForm, self).__init__(*args, **kwargs)
        for field in (self.fields['email'],self.fields['password']):
            field.widget.attrs.update({'class': 'form-control '})

    def clean(self):
        if self.is_valid():

            email = self.cleaned_data.get('email')
            password = self.cleaned_data.get('password')
            if not authenticate(email=email, password=password):
                raise forms.ValidationError('Invalid Login')

class AdminUpdateform(forms.ModelForm):
    """
      Updating User Info
    """
    class Meta:
        model  = Admin
        fields = ('email', 'username')
        widgets = {
                   'email':forms.TextInput(attrs={'class':'form-control'}),
                   'password':forms.TextInput(attrs={'class':'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        """
          specifying styles to fields 
        """
        super(AdminUpdateform, self).__init__(*args, **kwargs)
        for field in (self.fields['email'],self.fields['username']):
            field.widget.attrs.update({'class': 'form-control '})

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                admin = Admin.objects.exclude(pk = self.instance.pk).get(email=email)
            except Admin.DoesNotExist:
                return email
            raise forms.ValidationError("Email '%s' already in use." %email)
    def clean_username(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            try:
                admin = Admin.objects.exclude(pk = self.instance.pk).get(username=username)
            except Admin.DoesNotExist:
                return username
            raise forms.ValidationError("Username '%s' already in use." % username)


class productForm(forms.ModelForm):

    class Meta:

        model = m_Product
        fields = "__all__"

        