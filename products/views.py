from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.db.models import Q
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product
from .forms import ProductForm


class ProductListView(ListView):
    model = Product
    template_name = 'products/products.html'
    paginate_by = 8
    context_object_name = 'products'
    ordering = ['-created_at']

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['current_page'] = self.request.GET.get('page', 1)

        return context

    def get_queryset(self):
        try:
            query_set = super().get_queryset()
            search_query = self.request.GET.get('search')

            if search_query:
                query_set = query_set.filter(Q(name__icontains=search_query) | Q(description__icontains=search_query))

            return query_set
        except Exception as e:
            print(f"Error filtering products: {e}")
            return Product.objects.none()

# Create your views here.
class AddProduct(View):
    def post(self, request):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, f"Product '{product.name}' added successfully!")
            return redirect("inventory")
        else:
            # Add show_modal flag to indicate we need to reopen the modal
            products = Product.objects.all()
            return render(
                request,
                "inventory.html",
                {"products": products, "form": form, "show_modal": True},
            )


class AllProducts(View):
    def get(self, request):
        search_query = request.GET.get("q", "")
        if search_query:
            products = Product.objects.filter(name__icontains=search_query)
        else:
            products = Product.objects.all()
        form = ProductForm()
        return render(request, "inventory.html", {"products": products, "form": form})


class EditProduct(View):
    def get(self, request, slug):
        try:
            product = Product.objects.get(slug=slug)
            form = ProductForm(instance=product)
            return render(
                request,
                "inventory.html",
                {
                    "product": product,
                    "form": form,
                    "products": Product.objects.all(),
                    "show_modal": True,
                },
            )
        except Product.DoesNotExist:
            messages.error(request, "Product not found")
            return redirect("inventory")

    def post(self, request, slug):
        try:
            product = Product.objects.get(slug=slug)
            form = ProductForm(request.POST, request.FILES, instance=product)
            if form.is_valid():
                form.save()
                messages.success(
                    request, f"Product '{product.name}' updated successfully!"
                )
                return redirect("inventory")
            else:
                return render(
                    request,
                    "inventory.html",
                    {
                        "product": product,
                        "form": form,
                        "products": Product.objects.all(),
                        "show_modal": True,
                    },
                )
        except Product.DoesNotExist:
            messages.error(request, "Product not found")
            return redirect("inventory")


class DeleteProduct(View):
    def post(self, request, slug):
        try:
            product = Product.objects.get(slug=slug)
            product_name = product.name
            product.delete()
            messages.success(request, f"Product '{product_name}' deleted successfully!")
            return redirect("inventory")
        except Product.DoesNotExist:
            messages.error(request, "Product not found")
            return redirect("inventory")
