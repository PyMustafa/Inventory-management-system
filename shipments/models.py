from django.db import models
from products.models import Product
from django.contrib.auth import get_user_model
import random
from django.urls import reverse
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()


# Create your models here.


class Supplier(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("supplier-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


class Shipment(models.Model):
    PENDING = "PN"
    CONFIRMED = "CO"
    SHIPPED = "SH"
    DELIVERED = "DE"
    CANCELLED = "CA"
    STATUS_SHIPMENT_CHOICES = [
        (PENDING, "Pending"),
        (CONFIRMED, "Confirmed"),
        (SHIPPED, "Shipped"),
        (DELIVERED, "Delivered"),
        (CANCELLED, "Cancelled"),
    ]
    reference_number = models.CharField(max_length=15, unique=True)
    access_date = models.DateField()
    status = models.CharField(max_length=2, choices=STATUS_SHIPMENT_CHOICES, default=PENDING)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='created_shipments')
    confirmed_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='confirmed_shipments', blank=True,
                                     null=True)
    modified_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='modified_shipments', blank=True,
                                    null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def get_shipments_by_user(cls, user):
        return cls.objects.filter(created_by=user)

    def mark_as_confirmed(self, user):
        if self.status == self.PENDING:
            self.status = self.CONFIRMED
            self.confirmed_by = user
            self.save()

    def mark_as_shipped(self):
        if self.status == self.CONFIRMED:
            self.status = self.SHIPPED
            self.save()

    def mark_as_delivered(self):
        if self.status == self.SHIPPED:
            self.status = self.DELIVERED
            self.save()

    def mark_as_cancelled(self):
        if self.status != self.DELIVERED:
            self.status = self.CANCELLED
            self.save()

    def get_absolute_url(self):
        return reverse("shipment-detail", kwargs={"ref_num": self.reference_number})

    def __str__(self):
        return self.reference_number


def generate_reference_number():
    part1 = random.randint(100, 999)
    part2 = random.randint(100, 999)
    part3 = random.randint(100, 999)

    return f"{part1}-{part2}-{part3}"


@receiver(pre_save, sender=Shipment)
def set_reference_number(sender, instance, **kwargs):
    if not instance.reference_number:
        while True:
            reference_number = generate_reference_number()
            if not Shipment.objects.filter(reference_number=reference_number).exists():
                instance.reference_number = reference_number
                break


class ShipmentItem(models.Model):
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000)])

    def get_absolute_url(self):
        return reverse("shipmentitem-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.product.name} in {self.shipment.reference_number}"
