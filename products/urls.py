from django.urls import path
from .views import ProductListView, AddProduct, EditProduct, DeleteProduct

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path("product/", AddProduct.as_view(), name="add_product"),
    path("product/<slug:slug>/", EditProduct.as_view(), name="edit_product"),
    path(
        "product/<slug:slug>/delete/",
        DeleteProduct.as_view(),
        name="delete_product",
    ),
]
