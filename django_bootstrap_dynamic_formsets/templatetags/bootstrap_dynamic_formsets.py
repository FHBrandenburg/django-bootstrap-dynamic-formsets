from django import template
from django.utils.html import format_html

register = template.Library()

@register.inclusion_tag('django_bootstrap_dynamic_formsets/dynamic_formsets.html')
def bootstrap_dynamic_formset(formset, can_order=False, can_delete=False, form_wrapper="well", layout=""):
    return {"formset":formset, "can_order":can_order, "can_delete":can_delete, "form_wrapper":form_wrapper, "layout":layout}

@register.inclusion_tag('django_bootstrap_dynamic_formsets/dynamic_formsets_js.html',takes_context=True)
def bootstrap_dynamic_formset_js(context):
    return {'can_order':context['can_order'], 'can_delete':context['can_delete']}