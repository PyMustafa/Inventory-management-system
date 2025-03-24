from django.forms import ModelForm, RegexField
from django import forms
from .models import Supplier, Shipment
from django.core.exceptions import ValidationError


class SupplierForm(ModelForm):
    # Egyptian phone numbers starting with 010,011,012 or 015, followed by a 8-digit number
    phone = RegexField(
        regex=r"^01[0-2,5]\d{8}$",
        error_messages={
            "invalid": "Please enter a valid Egyptian phone number (e.g., 01xxxxxxxxx)."
        },
        required=True,
    )

    class Meta:
        model = Supplier
        fields = ["name", "address", "email", "phone"]

        error_messages = {
            "name": {
                "required": "Please enter the supplier name",
            },
            "address": {"required": "Please enter the supplier address"},
            "email": {
                "required": "Please enter the supplier email",
                "invalid": "Please enter a valid email address",
            },
        }
        labels = {
            "name": "Supplier Name",
            "address": "Address",
            "email": "Email",
            "phone": "Phone Number",
        }

    def clean_name(self):
        name = self.cleaned_data.get("name")

        # Only check uniqueness for new suppliers
        if not self.instance.pk and Supplier.objects.filter(name=name).exists():
            raise ValidationError("A supplier with this name already exists.")

        return name

    def clean_email(self):
        email = self.cleaned_data.get("email")

        # Only check uniqueness for new suppliers
        if not self.instance.pk and Supplier.objects.filter(email=email).exists():
            raise ValidationError("A supplier with this email already exists.")

        return email

    def clean_phone(self):
        phone = self.cleaned_data.get("phone")

        # Only check uniqueness for new suppliers
        if not self.instance.pk and Supplier.objects.filter(phone=phone).exists():
            raise ValidationError("A supplier with this phone number already exists.")

        return phone


class ShipmentForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = ["supplier", "status", "access_date"]
        widgets = {
            "supplier": forms.Select(attrs={"class": "form-select"}),
            "status": forms.Select(attrs={"class": "form-select"}),
            "access_date": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
        }
