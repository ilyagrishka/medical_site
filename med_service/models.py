from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=155, verbose_name="категория", unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=155, verbose_name="продукт", unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    image = models.ImageField(upload_to="photo_images", blank=True, null=True, verbose_name="Photo")
    price = models.IntegerField(default=0, verbose_name="цена")
    discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name="Скидка в %")
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name="Категория")

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ("id",)

    def __str__(self):
        return self.name

    def total_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)

        return self.price
