from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.views import View

from basket.mixins import BasketMixin
from basket.models import Basket
from basket.utils import get_user_basket
from med_service.models import Product


class BasketAddView(BasketMixin, View):
    def post(self, request):
        product_id = request.POST.get("product_id")
        product = Product.objects.get(id=product_id)

        basket = self.get_basket(request, product=product)

        if basket:
            basket.quantity += 1
            basket.save()
        else:
            Basket.objects.create(user=request.user if request.user.is_authenticated else None,
                                  session_key=request.session.session_key if not request.user.is_authenticated else None,
                                  product=product, quantity=1)

        response_data = {
            "message": "Товар добавлен в корзину",
            'cart_items_html': self.render_basket(request)
        }

        return JsonResponse(response_data)


class BasketChangeView(BasketMixin, View):
    def post(self, request):
        basket_id = request.POST.get("basket_id")

        basket = self.get_basket(request,basket_id=basket_id)

        basket.quantity = request.POST.get("quantity")
        basket.save()

        quantity = basket.quantity

        response_data = {
            "message": "Количество изменено",
            "quantity": quantity,
            'basket_items_html': self.render_basket(request)
        }

        return JsonResponse(response_data)


class BasketRemoveView(BasketMixin, View):
    def post(self, request):
        basket_id = request.POST.get("basket_id")

        basket = self.get_basket(request, basket_id=basket_id)
        quantity = basket.quantity
        basket.delete()

        response_data = {
            "message": "Товар удален из корзины",
            "quantity_deleted": quantity,
            'basket_items_html': self.render_basket(request)
        }

        return JsonResponse(response_data)
