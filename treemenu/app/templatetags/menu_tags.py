from django.template import Library, RequestContext

from ..models import SubMenu

register = Library()


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context: RequestContext, name: str = ''):
    objects = SubMenu.objects.select_related('category').filter(
        category__name=name)

    objects_dict = {}
    root = ''
    for object in objects:
        if object.parent is None:
            if root == '':
                root = object.category.name
            objects_dict[str(object.id)] = {'item': object, 'subitems': []}
        else:
            objects_dict[str(object.parent_id)]['subitems'].append(object)

    result = {'topmenu': root, 'data': list(objects_dict.values())}
    return {"result": result}
