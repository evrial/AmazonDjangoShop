from django.core.paginator import Paginator
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from amazon import fetch_category
from models import Category, Product, StaticPage

def home(request):
    categories = Category.objects.filter(visible=True).order_by('title')

    entries = Product.objects.filter(category__visible=True).order_by('popularity')[:10]
    return render_to_response('shop/index.html', {
    	'products': entries,
    	'categories': categories,
    	}, context_instance=RequestContext(request))

def category_view(request, slug):
    node = Category.objects.get(slug=slug)
    fetch_category(node.get_search_index_display(), node.amazon_node_id)

    product_entries = Product.objects.filter(category__slug=slug,
        category__visible=True).order_by('popularity')[:20]
    return render_to_response('shop/category_view.html', {
        'products': product_entries,
        'category': node,
        }, context_instance=RequestContext(request))

def product_page(request, cat_slug, asin):
    product = get_object_or_404(Product, asin=asin, category__slug=cat_slug,
        category__visible=True)

    return render_to_response('shop/product_page.html',{
        'product': product
        }, context_instance=RequestContext(request))


def static_page(request, slug):
    page = get_object_or_404(StaticPage, visible=True, slug=slug)
    return render_to_response('shop/static.html', {
    	'page': page,
    	}, context_instance=RequestContext(request))
