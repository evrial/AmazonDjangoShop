from django.shortcuts import render_to_response, get_object_or_404

from models import Category, Product, StaticPage

def home(request):
	categories = Category.objects.filter(visible=True)
	entries = Product.objects.filter(category__visible=True)[:10]
	return render_to_response('shop/index.html',
		{'products': entries, 'categories': categories})

def static(request, slug):
	page = get_object_or_404(StaticPage, slug=slug, visible=True)
	return render_to_response('shop/static.html', {'page': page})
