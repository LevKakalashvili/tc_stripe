import uuid
from django.db import models

# Create your models here.
class Item(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Идентификатор товара")
    name = models.CharField(max_length=70, unique=True, help_text="Наименование товара")
    description = models.CharField(max_length=20, help_text="Описание товара")
    price = models.DecimalField(max_digits=5, decimal_places=2, help_text="Цена товара")