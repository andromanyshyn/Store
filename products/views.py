from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.generic import ListView, TemplateView
from django.core.cache import cache

from .models import *
from common.views import TitleMixin


class IndexView(TitleMixin, TemplateView):
    title = 'Store'
    template_name = 'products/index.html'


class ListProductsView(TitleMixin, ListView):
    title = 'Store - Products'
    model = Products
    template_name = 'products/products.html'
    context_object_name = 'products'
    paginate_by = 3

    def get_queryset(self):
        queryset = super(ListProductsView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        if category_id:
            queryset = Products.objects.filter(category_id=category_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ListProductsView, self).get_context_data(**kwargs)
        categories = cache.get('categories')
        if not categories:
            context['categories'] = Categories.objects.all()
            cache.set('categories', context['categories'], 30)
        else:
            context['categories'] = categories
        return context


@login_required
def get_basket(request, product_id):
    product = Products.objects.get(id=product_id)
    basket = Basket.objects.filter(product=product, user=request.user)
    if basket:
        basket = basket.first()
        basket.quantity += 1
        basket.save()
    else:
        Basket.objects.create(product=product, user=request.user)
    return redirect(request.META['HTTP_REFERER'])


@login_required
def remove_basket(request, basket_object_id, user_id):
    basket_object = Basket.objects.get(id=basket_object_id, user=user_id)
    if basket_object.quantity > 1:
        basket_object.quantity -= 1
        basket_object.save()
    else:
        basket_object.delete()
    return redirect(request.META['HTTP_REFERER'])
