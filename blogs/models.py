from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок", help_text="Введите заголовок блога")
    article = models.TextField(verbose_name="Контент", help_text="Введите текст блога")
    image = models.ImageField(
        upload_to="images/",
        verbose_name="Превью",
        help_text="Загрузите превью блога",
        null=True,
        blank=True,
    )
    created_at = models.DateField(auto_now_add=True)
    publication_sign = models.BooleanField(verbose_name="Признак публикации")
    views = models.IntegerField(verbose_name="Количество просмотров", default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ["created_at"]
