from django import forms
from django.forms import ModelForm
from .models import Product
from django.core.exceptions import ValidationError


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "image", "critical_quantity"]

        error_messages = {
            "name": {
                "required": "Please enter the product name",
                "unique": "Product with this name already exists",
            },
            "description": {"required": "Please enter the product description"},
            "image": {"required": "Please upload an image"},
            "critical_quantity": {
                "required": "Please enter the critical quantity",
                "invalid": "Please enter a valid number",
            },
        }
        labels = {
            "name": "Product Name",
            "description": "Product Description",
            "image": "Product Image",
            "critical_quantity": "Critical Quantity",
        }
