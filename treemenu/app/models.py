from django.db import models


class CategoryMenu(models.Model,):
    name = models.CharField('Имя', max_length=255, unique=True)
    path = models.SlugField(
        'Элемент пути',
        max_length=500,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Menu category'
        verbose_name_plural = 'Menu categories'

    def get_absolute_url(self):
        return "/%s" % self.path

    def __str__(self):
        return self.name


class SubMenu(models.Model):
    name = models.CharField('Имя', max_length=255)
    path = models.SlugField(
        'Элемент пути',
        max_length=500,
        blank=True,
        null=True
    )

    category = models.ForeignKey(
        CategoryMenu,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name='category'

    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='child'
    )

    class Meta:
        verbose_name = 'submenu'
        verbose_name_plural = 'submenu items'

    def get_absolute_url(self):
        return "/%s" % self.path

    def __str__(self):
        return self.name
