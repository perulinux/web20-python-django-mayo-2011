#!/usr/bin/env python
# -*- encoding: utf8 -*-

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from models import Book
from forms import OrderForm

def latest_books(request):
    book_list = Book.objects.order_by('-pub_date')[:10]
    return render_to_response('books/latest_books.html', {'book_list': book_list})

def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('latest_books'))
    else:
        form = OrderForm()
        return render_to_response(
            'books/create_order.html', 
            {'form': form}
        )
