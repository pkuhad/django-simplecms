from django import template

from ..models import Page

register = template.Library()

@register.inclusion_tag('pages/page-block.html')
def page_block():
    pages = Page.objects.all()[:5]
    return {'pages':pages}

