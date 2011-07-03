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
    """
    Processes an book order from customers
    """
    print request.session.session_key
    print dict(request.session)
    if request.user.has_perm('user.send_tweet'):
        print "Si puede twittear"
    else:
        print "No puede twittear"
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # This decrements the number of books in stock
            # for the requested book
            order = form.save()
            return HttpResponseRedirect(reverse('latest_books'))
    return render_to_response(
        'books/create_order.html', 
        {'form': form}
    )
