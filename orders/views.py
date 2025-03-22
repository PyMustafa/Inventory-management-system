from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Order, OrderItem


class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = "orders/order_list.html"
    context_object_name = "orders"
    paginate_by = 10

    def get_queryset(self):

        try:
            query_set = super().get_queryset()
            search_query = self.request.GET.get('search')

            if search_query:
                query_set = query_set.filter(
                    Q(name__icontains=search_query) | Q(description__icontains=search_query))

            return query_set
        except Exception as e:
            print(f"Error filtering products: {e}")
            return Order.objects.none()


class OrderDetailView(DetailView):
    model = Order
    template_name = 'orders/order_detail.html'
    context_object_name = 'order'


class OrderItemListView(ListView):
    model = OrderItem
    template_name = 'orders/orderitem_list.html'
    context_object_name = 'orderitems'
    paginate_by = 10

    def get_queryset(self):

        try:
            query_set = super().get_queryset()
            search_query = self.request.GET.get('search')

            if search_query:
                query_set = query_set.filter(
                    Q(name__icontains=search_query) | Q(description__icontains=search_query))

            return query_set
        except Exception as e:
            print(f"Error filtering products: {e}")
            return OrderItem.objects.none()


class OrderItemDetailView(DetailView):
    model = OrderItem
    template_name = 'orders/orderitem_detail.html'
    context_object_name = 'orderitem'

# Create your views here.
