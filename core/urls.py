from django.urls import path
from .views import (
    ItemDetailView,
    CheckoutView,
    HomeView,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    PaymentView,
    AddCouponView,
    RequestRefundView
)
from django.http import HttpResponse
from django.views import View


# --- Safe placeholder classes to prevent NameError ---

class CategoryItemListView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Category placeholder page")


class SearchResultsView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Search results placeholder")


class AddReviewView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Add review placeholder")


# --- URL patterns ---

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<str:category>/', CategoryItemListView.as_view(), name='category'),
    path('search/', SearchResultsView.as_view(), name='search'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('add-review/<slug:slug>/', AddReviewView.as_view(), name='add-review'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
]
