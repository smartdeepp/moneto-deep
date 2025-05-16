from django import template
from wagtail.models import Site

register = template.Library()


@register.simple_tag(takes_context=True)
def get_site_root(context):
    return Site.find_for_request(context["request"]).root_page


def has_menu_children(page):
    return page.get_children().live().in_menu().exists()

def get_links(context, parent, calling_page):
    menu_items = parent.get_children().live().in_menu()
    for menuitem in menu_items:
        menuitem.show_dropdown = has_menu_children(menuitem)
        menuitem.active = (
            calling_page.url_path.startswith(menuitem.url_path)
            if calling_page
            else False
        )
    return {
        "calling_page": calling_page,
        "menuitems": menu_items,
        "request": context["request"],
    }


@register.inclusion_tag("partials/_navlinks.html", takes_context=True)
def top_menu(context, parent, calling_page=None):
    return get_links(context, parent, calling_page)


@register.inclusion_tag("partials/_footer_navlinks.html", takes_context=True)
def bottom_menu(context, parent, calling_page=None):
    return get_links(context, parent, calling_page)
