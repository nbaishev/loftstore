import uuid

from django.core.exceptions import ObjectDoesNotExist
from django.db import models

from users.models import User


class GetOrNoneManager(models.Manager):
    """returns none if object doesn't exist else model instance"""

    def get_or_none(self, **kwargs):
        try:
            return self.get(**kwargs)
        except ObjectDoesNotExist:
            return None


class BaseModel(models.Model):

    class Meta:
        abstract = True
        ordering = ('-created_at',)

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    created_at = models.DateTimeField(
        'Дата создания',
        auto_now_add=True,
        db_index=True
    )
    updated_at = models.DateTimeField(
        'Дата изменения',
        auto_now=True
    )
    objects = GetOrNoneManager()

    def str(self):
        return self.id.hex


class Order(BaseModel):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='orders'
    )
    total_cost = models.DecimalField(
        verbose_name='Сумма заказа',
        max_digits=8,
        decimal_places=2,
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class ProductsInOrder(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='customer',
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        verbose_name='Товар',
        related_name='order',
    )
    quantity = models.IntegerField(
        verbose_name='Сумма заказа',
        blank=True,
    )

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'
