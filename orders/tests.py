from django.test import TestCase

import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from carts.models import Cart
from goods.models import Products
from orders.models import Order, OrderItem

User = get_user_model()


@pytest.fixture
def user(db):
    return User.objects.create_user(username='testuser', password='testpass')


@pytest.fixture
def cart_item(db, user):
    # Создадим товар в корзине для пользователя
    product = Products.objects.create(name='Test Product', sku='TP001', quantity=10, price=100)
    return Cart.objects.create(user=user, product=product, quantity=2)


@pytest.mark.django_db
def test_create_order_view_success(client, user, cart_item):
    client.login(username='testuser', password='testpass')

    url = reverse('orders:create_order')
    response = client.post(url, {
        'phone_number': '1234567890',
        'payment_on_get': True
    })

    assert response.status_code == 302  # Проверка на редирект
    assert Order.objects.count() == 1  # Заказ должен быть создан
    assert OrderItem.objects.count() == 1  # Товар в заказе должен быть
    assert Cart.objects.count() == 0  # Корзина должна быть очищена


@pytest.mark.django_db
def test_create_order_view_insufficient_stock(client, user):
    client.login(username='testuser', password='testpass')

    # Создаем товар с недостаточным количеством
    product = Products.objects.create(name='Test Product', sku='TP002', quantity=1, price=100)
    Cart.objects.create(user=user, product=product, quantity=2)

    url = reverse('orders:create_order')
    response = client.post(url, {
        'phone_number': '1234567890',
        'payment_on_get': True
    })

    assert response.status_code == 302  # Проверка на редирект
    assert Order.objects.count() == 0  # Заказ не должен быть создан
    assert Cart.objects.count() == 1  # Корзина должна остаться неизменной
    # Проверка наличия сообщения об ошибке в сессии
    assert 'Недостаточное количество товара ' in str(response.content)


@pytest.mark.django_db
def test_create_order_view_invalid_form(client, user):
    client.login(username='testuser', password='testpass')

    url = reverse('orders:create_order')
    response = client.post(url, {})  # Пустая форма

    assert response.status_code == 302  # Проверка на редирект
    assert 'Заполните все обязательные поля!' in str(response.content)

