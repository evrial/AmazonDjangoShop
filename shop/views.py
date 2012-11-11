from django.shortcuts import render_to_response

from models import Product

def home(request):
	entries = Product.objects.all()[:10]
	return render_to_response('index.html', {'products': entries})