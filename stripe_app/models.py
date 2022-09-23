import decimal
import uuid
from typing import NamedTuple

from django.db import models

class ItemNamedTuple(NamedTuple):
    uuid: uuid.UUID
    name: str
    name: str
    description: str
    price: decimal.Decimal


# Create your models here.
class Item(models.Model):
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Идентификатор товара",
                            verbose_name="Идентификатор", editable=False)
    name = models.CharField(max_length=200, unique=True, blank=False, default='', help_text="Наименование товара",
                            verbose_name="Наименование")
    description = models.CharField(max_length=500, blank=True, help_text="Описание товара", verbose_name="Описание")
    price = models.DecimalField(max_digits=5, decimal_places=2, help_text="Цена товара", verbose_name="Цена")
    # price = models.IntegerField(help_text="Цена товара", verbose_name="Цена")

    def __str__(self):
        return self.name

    def get_tuple(self) -> ItemNamedTuple:
        return ItemNamedTuple(
            uuid=self.uuid,
            name=self.name,
            price=self.price,
            description=self.description,
        )

