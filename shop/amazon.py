import caching

from models import Category, Product
from amazonproduct.errors import AWSError

# Amazon Product Advertising API
AWS_KEY = 'AKIAJXBYRCZ7AKW6USBA'
SECRET_KEY = '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'
ASSOCIATE_TAG = 'onlinshop0b-20'


def fetch_category(search_index, amazon_node_id):
    api = caching.ResponseCachingAPI(AWS_KEY, SECRET_KEY, 'us', ASSOCIATE_TAG,
    cachedir='cache', cachetime=86400)

    try:
        for root in api.item_search(search_index, BrowseNode=str(amazon_node_id), ResponseGroup='\
            EditorialReview,Images,ItemAttributes,ItemIds,OfferFull,Offers,Reviews,SalesRank'):

            for p in root.Items.Item:
                g = Product()
                g.category = Category.objects.get(amazon_node_id=amazon_node_id)
                g.asin = unicode(p.ASIN)
                g.title = unicode(p.ItemAttributes.Title)
                try:
                    g.popularity = unicode(p.SalesRank)
                except:
                    g.popularity = 666
                try:
                    if hasattr(p.ItemAttributes, 'ListPrice'):
                        g.price = unicode(p.ItemAttributes.ListPrice.FormattedPrice)
                    elif hasattr(p.OfferSummary, 'LowestUsedPrice'):
                        g.price =  u'used from %s' % p.OfferSummary.LowestUsedPrice.FormattedPrice
                except:
                    g.price = None
                try:
                    g.description = unicode(p.EditorialReviews.EditorialReview.Content)
                except:
                    g.description = None
                try:
                    g.medium_image = unicode(p.MediumImage.URL)
                    g.large_image = unicode(p.LargeImage.URL)
                except:
                    pass
                try:
                    g.manufacturer = unicode(p.ItemAttributes.Manufacturer)
                except:
                    g.manufacturer = "unknown"
                g.save()

    except AWSError, e:
        if e.code == 'AWS.ParameterOutOfRange':
            pass
