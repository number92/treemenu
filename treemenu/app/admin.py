from django.contrib import admin

from .models import CategoryMenu, SubMenu


@admin.register(CategoryMenu)
class CategoryMenuAdmin(admin.ModelAdmin):

    fields = ['name', 'path']
    list_display = ['__str__',]


@admin.register(SubMenu)
class SubMenuAdmin(admin.ModelAdmin):

    fields = ['name', 'category', 'path', 'parent',]
    list_display = ['__str__', 'category', 'path', 'parent',]
