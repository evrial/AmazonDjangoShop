from amazonproduct.api import API
from amazonproduct.contrib import caching
from amazonproduct.errors import AWSError

from django.conf import settings
from django.core.exceptions import ValidationError
from .models import Category, Product


def fetch_category(search_index, amazon_node_id):
    category = Category.objects.get(amazon_node_id=amazon_node_id)
    api = caching.ResponseCachingAPI(
        settings.AMAZON_ACCESS_KEY,
        settings.AMAZON_SECRET_KEY,
        settings.AMAZON_API_LOCALE,
        settings.AMAZON_ASSOCIATE_TAG,
        cachedir='cache',
        cachetime=86400)

    try:
        for root in api.item_search(search_index, BrowseNode=str(amazon_node_id),
            ResponseGroup=settings.AMAZON_RESPONSE_GROUP):

            for item in root.Items.Item:
                fields = {
                    'asin': item.ASIN,
                    'category': category,
                    'title': item.ItemAttributes.Title,
                    'detailpageurl': item.DetailPageURL,
                    'manufacturer': getattr(item.ItemAttributes, 'Manufacturer', None),
                    'publisher': getattr(item.ItemAttributes, 'Publisher', None),
                    'brand': getattr(item.ItemAttributes, 'Brand', None),
                    'popularity': getattr(item, 'SalesRank', 0),
                    'price': None,
                }
                
                if hasattr(item, 'MediumImage'):
                    fields['medium_image'] = getattr(item.MediumImage, 'URL', None)
                if hasattr(item, 'LargeImage'):
                    fields['large_image'] = getattr(item.LargeImage, 'URL', None)
                if hasattr(item, 'EditorialReviews'):
                    fields['description'] = getattr(item.EditorialReviews.EditorialReview, 'Content', None)
                if hasattr(item.Offers, 'Offer'):
                    fields['price'] = item.Offers.Offer.OfferListing.Price.FormattedPrice.pyval
                elif hasattr(item.ItemAttributes, 'ListPrice'):
                    fields['price'] = item.ItemAttributes.ListPrice.FormattedPrice.pyval
                elif hasattr(item.OfferSummary, 'LowestUsedPrice'):
                    fields['price'] =  'used from %s' % item.OfferSummary.LowestUsedPrice.FormattedPrice.pyval

                obj, created = Product.objects.update_or_create(**fields)

    except AWSError as e:
        if e.code == 'AWS.ParameterOutOfRange':
            pass # reached the api limit of 10 pages
        else:
            raise ValidationError(message=e.msg)

def create_cart(asin, quantity=1):
    api = API(
        settings.AMAZON_ACCESS_KEY,
        settings.AMAZON_SECRET_KEY,
        settings.AMAZON_API_LOCALE,
        settings.AMAZON_ASSOCIATE_TAG)
    cart = api.cart_create({asin: quantity})

    try:
        return cart.Cart.PurchaseURL
    except (ValueError, InvalidCartItem):
        raise ValidationError()
