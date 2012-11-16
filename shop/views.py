from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from amazon import fetch
from models import Category, Product, StaticPage

def home(request):
    categories = Category.objects.filter(visible=True).order_by('title')

    entries = Product.objects.all().order_by('popularity')[:10]
    return render_to_response('shop/index.html', {
    	'products': entries,
    	'categories': categories,
    	}, context_instance=RequestContext(request))

def category_view(request, slug):
    node = Category.objects.get(slug=slug)
    fetch(node.amazon_node_id)

    product_entries = Product.objects.filter(category__slug=slug).order_by('popularity')[:10]
    return render_to_response('shop/category_view.html', {
        'products': product_entries,
        'category': node,
        }, context_instance=RequestContext(request))

def static_page(request, slug):
    page = get_object_or_404(StaticPage, visible=True, slug=slug)
    return render_to_response('shop/static.html', {
    	'page': page,
    	}, context_instance=RequestContext(request))
