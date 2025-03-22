from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
import re

# Get the User model
user = get_user_model()

# Define role choices for the role field
role_choices = [
    ('manager', 'Manager'),
    ('employee', 'Employee'),
]


class UserRegisterForm(UserCreationForm):
    # Define form fields with required attributes
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    username = forms.CharField(required=True)

    # Role field with choices and custom widget attributes
    role = forms.ChoiceField(choices=role_choices, required=True, widget=forms.Select(attrs={
        'class': 'form-select'
    }))

    class Meta:
        # Specify the model and fields to include in the form
        model = user
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')

    def clean(self):
        # Override the clean method to add custom validation
        data = super().clean()
        password1 = data.get('password1')
        password2 = data.get('password2')

        # Check if passwords match
        if password1 != password2:
            raise forms.ValidationError('Passwords must match')

        return data

    def clean_email(self):
        # Validate email uniqueness
        email = self.cleaned_data.get('email')
        # Exclude the current instance's email during updates
        filter_email = user.objects.filter(email=email).exclude(email=self.instance.email)
        if filter_email.exists():
            raise forms.ValidationError('Email already exists')
        return email

    def clean_first_name(self):
        # Validate first name
        first_name = self.cleaned_data.get('first_name')
        pattern = r'^[A-Za-z]+$'  # Regex to allow only alphabets
        if not re.match(pattern, first_name):
            raise forms.ValidationError('First name must contain only alphabets')
        # Check length constraints
        if len(first_name) < 2 or len(first_name) > 10:
            raise forms.ValidationError('First name must be between 2 and 10 characters')
        return first_name

    def clean_last_name(self):
        # Validate last name
        last_name = self.cleaned_data.get('last_name')
        pattern = r'^[A-Za-z]+$'  # Regex to allow only alphabets
        if not re.match(pattern, last_name):
            raise forms.ValidationError('Last name must contain only alphabets')
        # Check length constraints
        if len(last_name) < 2 or len(last_name) > 10:
            raise forms.ValidationError('Last name must be between 2 and 10 characters')

        return last_name

    def clean_username(self):
        # Validate username
        username = self.cleaned_data['username']
        # Exclude the current instance's username during updates
        filter_username = user.objects.filter(username=username).exclude(username=self.instance.username)
        # Regex to allow alphanumeric characters and ._-
        pattern = r'^[a-zA-Z0-9_.-]+$'
        if not re.match(pattern, username):
            raise forms.ValidationError('Username must contain only alphabets, numbers, and ._-')
        # Check if username already exists
        if filter_username.exists():
            raise forms.ValidationError('Username already exists')
        return username

    def save(self, commit=True):
        # Override the save method to handle role assignment
        user = super().save(commit=False)
        role = self.cleaned_data.get('role')

        # Assign is_staff based on the selected role
        if role == 'manager':
            user.is_staff = True
        elif role == 'employee':
            user.is_staff = False

        # Save the user if commit is True
        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        # Customize form field attributes during initialization
        super().__init__(*args, **kwargs)
        # Add Bootstrap classes to all fields except 'role'
        for field_name, field in self.fields.items():
            if field_name != 'role':
                field.widget.attrs['class'] = 'form-control'

        # Add custom attributes to specific fields
        self.fields['first_name'].widget.attrs.update({
            'id': 'f_name',
            'placeholder': 'Enter first name'
        })
        self.fields['last_name'].widget.attrs.update({
            'id': 'l_name',
            'placeholder': 'Enter last name'
        })
        self.fields['username'].widget.attrs.update({
            'id': 'username',
            'placeholder': 'Username will be generated from email',
        })
        self.fields['email'].widget.attrs.update({
            'id': 'email',
            'placeholder': 'Enter your email'
        })
        self.fields['password1'].widget.attrs.update({
            'id': 'password',
            'placeholder': 'Create a password'
        })
        self.fields['password2'].widget.attrs.update({
            'id': 'confirm_password',
            'placeholder': 'Confirm your password'
        })
        self.fields['role'].widget.attrs.update({
            'id': 'role'
        })
