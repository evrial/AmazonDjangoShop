from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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
    category = Category.objects.get(slug=slug)
    fetch_category(category.get_search_index_display(), category.amazon_node_id)

    product_entries = Product.objects.filter(category__slug=slug,
        category__visible=True).order_by('popularity') #[:20]
    paginator = Paginator(product_entries, 20)

    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = paginator.page(paginator.num_pages)

    return render_to_response('shop/category_view.html', {
        'products': products,
        'category': category,
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
