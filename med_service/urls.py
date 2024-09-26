from django.urls import path

from med_service import views

app_name = 'med_service'

urlpatterns = [
    path("<slug:category_slug>/", views.CatalogView.as_view(), name="index"),
    path("search/", views.CatalogView.as_view(), name="search"),
    path("service/<slug:product_slug>/", views.ServiceView.as_view(), name="service"),
]
