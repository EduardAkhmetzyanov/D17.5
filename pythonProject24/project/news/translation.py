from .models import Category, News
from modeltranslation.translator import register, \
    TranslationOptions


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'subscribers')


@register(News)
class MyModelTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'category', 'time_create', 'author')
