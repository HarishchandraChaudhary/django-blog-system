from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','user_type',
                  'phone','specialization','password1','password2')
        widgets = {fld: forms.TextInput(attrs={'class':'form-control'}) for fld in fields}
