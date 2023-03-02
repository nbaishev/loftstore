import uuid

from django.db import models


class Product(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    name = models.CharField(
        verbose_name='Название',
        max_length=150,
        blank=True
    )
    category = models.CharField(
        verbose_name='Категория',
        max_length=150,
        blank=True
    )
    description = models.CharField(
        verbose_name='Описание',
        max_length=150,
        blank=True
    )
    price = models.DecimalField(
        verbose_name='Цена',
        max_digits=8,
        decimal_places=2,
    )
    quantity_in_stock = models.IntegerField(
        verbose_name='Количество',
        blank=True
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name
