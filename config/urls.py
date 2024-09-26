from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from config import settings
from config.settings import DEBUG

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("sigma.urls", namespace="sigma")),
    path("catalog", include("med_service.urls", namespace="catalog")),
    path("user/", include("users.urls", namespace="user")),
    path("basket/", include("basket.urls", namespace="basket")),
    path("orders/", include("orders.urls", namespace="orders")),

]

if DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
