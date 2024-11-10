from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='')






    # наименование,
    # описание,
    # изображение,
    # категория,
    # цена за покупку,
    # дата создания,
    # дата последнего изменения.
