from django.urls import path
from . import views

urlpatterns = [
    path("", views.add_order, name="add-order"),
    path("order/", views.OrderListView.as_view(), name="order-list"),
    path("order/<int:pk>/", views.OrderDetailView.as_view(), name="order-detail"),
    path("orderitem/", views.OrderItemListView.as_view(), name="orderitem-list"),

]
