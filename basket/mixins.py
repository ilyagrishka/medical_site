from django.template.loader import render_to_string
from django.urls import reverse

from basket.models import Basket


class BasketMixin:

    def get_basket(self, request, product=None, cart_id=None):

        if request.user.is_authenticated:
            query_kwargs = {"user": request.user}
        else:
            query_kwargs = {"session_key": request.session.session_key}

        if product:
            query_kwargs["product"] = product
        if cart_id:
            query_kwargs["id"] = cart_id

        return Basket.objects.filter(**query_kwargs).first()

    def render_basket(self, request):
        user_basket = get_user_baskets(request)
        context = {"baskets": user_basket}

        referer = request.META.get('HTTP_REFERER')
        if reverse('orders:create_order') in referer:
            context["order"] = True

        return render_to_string(
            "basket/included_basket.html", context, request=request
        )

