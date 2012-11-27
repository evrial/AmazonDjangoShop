import AmazonDjangoShop.settings as settings
import caching

from django.core.exceptions import ValidationError
from amazonproduct.api import API
from amazonproduct.errors import AWSError
from models import Category, Product

def fetch_category(search_index, amazon_node_id):
    api = caching.ResponseCachingAPI(
        settings.AMAZON_AWS_KEY,
        settings.AMAZON_SECRET_KEY,
        settings.AMAZON_API_LOCALE,
        settings.AMAZON_ASSOCIATE_TAG,
        cachedir='cache',
        cachetime=86400)

    try:
        for root in api.item_search(search_index, BrowseNode=str(amazon_node_id),
            ResponseGroup='EditorialReview,Images,ItemAttributes,ItemIds,Offers,Reviews,SalesRank'):

            for item in root.Items.Item:
                product = Product()
                product.category = Category.objects.get(amazon_node_id=amazon_node_id)
                product.asin = item.ASIN
                product.title = unicode(item.ItemAttributes.Title)
                product.detailpageurl = unicode(item.DetailPageURL)
                product.manufacturer = unicode(getattr(item.ItemAttributes, 'Manufacturer', None))
                product.publisher = unicode(getattr(item.ItemAttributes, 'Publisher', None))
                product.brand = unicode(getattr(item.ItemAttributes, 'Brand', None))
                product.medium_image = getattr(item.MediumImage, 'URL', None)
                product.large_image = getattr(item.LargeImage, 'URL', None)
                product.popularity = getattr(item, 'SalesRank', 1000)

                if hasattr(item, 'EditorialReviews'):
                    product.description = unicode(getattr(item.EditorialReviews.EditorialReview, 'Content', None))

                if hasattr(item.Offers, 'Offer'):
                    product.price = item.Offers.Offer.OfferListing.Price.FormattedPrice.pyval
                elif hasattr(item.ItemAttributes, 'ListPrice'):
                    product.price = item.ItemAttributes.ListPrice.FormattedPrice.pyval
                elif hasattr(item.OfferSummary, 'LowestUsedPrice'):
                    product.price =  u'used from %s' % item.OfferSummary.LowestUsedPrice.FormattedPrice.pyval
                else:
                    product.price = None
                product.save()

    except AWSError, e:
        if e.code == 'AWS.ParameterOutOfRange':
            pass # reached the api limit of 10 pages
        else:
            raise ValidationError(message=e)

def create_cart(asin, quantity=1):
    api = API(
        settings.AMAZON_AWS_KEY,
        settings.AMAZON_SECRET_KEY,
        settings.AMAZON_API_LOCALE,
        settings.AMAZON_ASSOCIATE_TAG)
    cart = api.cart_create({asin: quantity})

    return unicode(cart.Cart.PurchaseURL)