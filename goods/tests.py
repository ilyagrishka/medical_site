

import pytest
from django.urls import reverse
from django.http import Http404
from goods.models import Products


@pytest.mark.django_db
def test_catalog_view_empty_database(client):
    response = client.get(reverse('catalog', kwargs={'category_slug': 'some_category'}))
    assert response.status_code == 404


@pytest.mark.django_db
def test_catalog_view_with_products(client):
    # Создание тестовых данных
    category = Products.objects.create(name="test_category", slug="some_category")
    product1 = Products.objects.create(name="Product 1", slug="product-1", category=category)
    product2 = Products.objects.create(name="Product 2", slug="product-2", category=category)

    response = client.get(reverse('catalog', kwargs={'category_slug': 'some_category'}))
    assert response.status_code == 200
    assert len(response.context['goods']) == 2


@pytest.mark.django_db
def test_product_view(client):
    product = Products.objects.create(name="Test Product", slug="test-product")

    response = client.get(reverse('product', kwargs={'product_slug': 'test-product'}))
    assert response.status_code == 200
    assert response.context['product'].name == "Test Product"


@pytest.mark.django_db
def test_product_view_not_found(client):
    # Проверка на несуществующий продукт
    with pytest.raises(Http404):
        client.get(reverse('product', kwargs={'product_slug': 'non-existent-product'}))
