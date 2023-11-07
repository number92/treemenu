import sys
import logging

from django.core.management.base import BaseCommand

from app.models import SubMenu, CategoryMenu


logging.basicConfig(
        level=logging.INFO,
        stream=sys.stdout,
        encoding='utf-8',
        format='%(levelname)s, %(message)s',
    )


class Command(BaseCommand):
    '''Заполнение тестовыми данными БД'''
    help = "Создание меню"

    def handle(self, *args, **kwargs):
        for obj in range(1, 4):
            menu = CategoryMenu.objects.create(name=f'Menu {obj}')
            menu.save()
            self.generate_item(menu, obj)
        logging.info('тестовые данные добавлены')

    def generate_item(self, menu: CategoryMenu, obj: int):
        name = f'Submenu {obj}'
        subitem = SubMenu(name=name, category=menu)
        subitem.save()
        logging.debug(f'Submenu {obj} добавлено')
        self.generate_item_list(subitem, menu)

    @staticmethod
    def generate_item_list(subitem: SubMenu, menu: CategoryMenu) -> list:
        objects = SubMenu.objects.bulk_create(
            [
                SubMenu(name="Subsubmenu 1", category=menu, parent=subitem),
                SubMenu(name="Subsubmenu 2", category=menu, parent=subitem),
                SubMenu(name="Subsubmenu 3", category=menu, parent=subitem),
            ]
        )
        logging.debug('Дочерние подменю добавлены')
        return objects
