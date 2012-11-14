import caching

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from models import Category, Product, StaticPage

AWS_KEY = 'AKIAJXBYRCZ7AKW6USBA'
SECRET_KEY = '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'
ASSOCIATE_TAG = 'onlinshop0b-20'


def fetch(amazon_node_id):
    api = caching.ResponseCachingAPI(AWS_KEY, SECRET_KEY, locale='us',
        associate_tag=ASSOCIATE_TAG, cachedir='cache', cachetime=600)

    category = api.browse_node_lookup(browse_node_id=str(amazon_node_id),
        response_group='TopSellers')

    for i in category.BrowseNodes.BrowseNode.TopSellers.TopSeller:
        for j in i.ASIN:
            product = api.item_lookup(item_id=str(j), ResponseGroup="\
                EditorialReview,Images,ItemAttributes,ItemIds,OfferFull,Offers,Reviews,SalesRank")
            for p in product.Items.Item:
                g = Product()
                g.category = amazon_node_id
                g.asin = unicode(p.ASIN)
                g.title = unicode(p.ItemAttributes.Title)
                g.popularity = unicode(p.SalesRank)
                try:
                    if hasattr(p.ItemAttributes, 'ListPrice'):
                        g.price = unicode(p.ItemAttributes.ListPrice.FormattedPrice)
                    elif hasattr(p.OfferSummary, 'LowestUsedPrice'):
                        g.price =  u'used from %s' % p.OfferSummary.LowestUsedPrice.FormattedPrice
                except:
                        g.price = 'No price'

                g.description = unicode(p.EditorialReviews.EditorialReview.Content)
                g.medium_image = unicode(p.MediumImage.URL)
                g.large_image = unicode(p.LargeImage.URL)
                try:
                    g.manufacturer = unicode(p.ItemAttributes.Manufacturer)
                except:
                    g.manufacturer = "unknown"
                g.save()

def home(request):
    categories = Category.objects.filter(visible=True).order_by('title')

    entries = Product.objects.all().order_by('-popularity')[:10]
    return render_to_response('shop/index.html', {
    	'products': entries,
    	'categories': categories,
    	}, context_instance=RequestContext(request))

def category_view(request, node_id):
    fetch(node_id)

    entries = Product.objects.filter(category=node_id).order_by('-popularity')[:10]
    return render_to_response('shop/category_view.html', {
        'category': entries,
        }, context_instance=RequestContext(request))

def static_page(request, slug):
    page = get_object_or_404(StaticPage, visible=True, slug=slug)
    return render_to_response('shop/static.html', {
    	'page': page,
    	}, context_instance=RequestContext(request))
