from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext

from amazon import fetch_category, create_cart
from models import Category, Product, StaticPage

noimage = 'http://placehold.it/150x150'

def home(request):
    categories = Category.objects.filter(visible=True).order_by('title')
    entries = Product.objects.select_related().filter(category__visible=True).order_by('popularity')[:12]
    return render_to_response('shop/index.html', {
    	'products': entries,
    	'categories': categories,
        'noimage': noimage,
    	}, context_instance=RequestContext(request))

def category_view(request, slug):
    categories = Category.objects.filter(visible=True).order_by('title')
    category = Category.objects.get(slug=slug)
    fetch_category(category.get_search_index_display(), category.amazon_node_id)

    product_entries = Product.objects.select_related().filter(
        category__slug=slug,
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
        'categories': categories,
        'category': category,
        'noimage': noimage,
        }, context_instance=RequestContext(request))

def product_page(request, cat_slug, asin):
    quantity = request.GET.get('addtocart')
    if quantity and quantity.isdigit():
        return redirect(create_cart(asin, quantity))

    categories = Category.objects.filter(visible=True).order_by('title')
    product = get_object_or_404(Product, asin=asin, category__slug=cat_slug,
        category__visible=True)

    return render_to_response('shop/product_page.html',{
        'product': product,
        'categories': categories,
        }, context_instance=RequestContext(request))

def static_page(request, slug):
    categories = Category.objects.filter(visible=True).order_by('title')
    page = get_object_or_404(StaticPage, visible=True, slug=slug)
    return render_to_response('shop/static_page.html', {
    	'page': page,
        'categories': categories,
    	}, context_instance=RequestContext(request))
