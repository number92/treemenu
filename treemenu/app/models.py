from django.db import models


class GeneralFieldMenu(models.Model):
    name = models.CharField('Имя', max_length=255, unique=True)
    path = models.SlugField(
        'Элемент пути',
        max_length=500,
        blank=True,
        null=True
    )

    class Meta:
        abstract = True

    def get_absolute_url(self):
        return "/%s" % self.path

    def __str__(self):
        return self.name


class CategoryMenu(GeneralFieldMenu, models.Model,):

    class Meta:
        verbose_name = 'Menu category'
        verbose_name_plural = 'Menu categories'

    def __str__(self):
        return self.name


class SubMenu(GeneralFieldMenu, models.Model):
    name = models.CharField('Имя', max_length=255, unique=True)
    category = models.ForeignKey(
        CategoryMenu,
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_DEFAULT,
        null=True,
        blank=True,
        default=0
    )

    class Meta:
        verbose_name = 'submenu'
        verbose_name_plural = 'submenu items'
