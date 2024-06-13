from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from .models import CustomUser

class SignupForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password-input'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2')

        def save(self, commit=True):
            user = super().save(commit=False)
            user.first_name = self.cleaned_data["first_name"]
            if commit:
                user.save()
            return user

