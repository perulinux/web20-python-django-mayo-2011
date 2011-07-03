#!/usr/bin/env python
# -*- encoding: utf8 -*-

from django.contrib import admin
from django.utils.translation import ugettext as _
from models import *
from django.contrib.auth.models import Permission

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'lastname', 'firstname', 'website', 
                    'number_of_books', )
    ordering = ('lastname', 'firstname', 'website', )

    def number_of_books(self, instance):
        return instance.book_set.count()

    number_of_books.short_description = _(u'Número de libros')

def update_stock(modeladmin, request, queryset):
    for book in queryset.all():
        book.stock += 10
        book.save()

update_stock.short_description = _(u"Agregar 10 unidades a stock")

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'stock', 'pub_date', )
    list_filter = ('author', )
    search_fields = ('title', 'author__lastname', 'author__firstname', )
    actions = (update_stock, )
    ordering = ('id', )
    list_per_page = 2

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Order)
admin.site.register(Permission)
