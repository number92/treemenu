from django.db import models


class CategoryMenu(models.Model):
    name = models.CharField('Имя', max_length=255)

    class Meta:
        verbose_name = 'Menu category'
        verbose_name_plural = 'Menu categories'

    def __str__(self):
        return self.verbose_name


class TreeMenu(models.Model):
    name = models.CharField('Имя', max_length=255)
    category = models.ForeignKey(
        CategoryMenu,
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )
    path = models.CharField(max_length=500, blank=True, null=True, unique=True)
    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_DEFAULT,
        null=True,
        blank=True,
        default=0
    )

    class Meta:
        verbose_name = 'Menu item'
        verbose_name_plural = 'Menu items'

    def __str__(self):
        return self.name
