import caching

AWS_KEY = 'AKIAJXBYRCZ7AKW6USBA'
SECRET_KEY = '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'
ASSOCIATE_TAG = 'onlinshop0b-20'


api = caching.ResponseCachingAPI(AWS_KEY, SECRET_KEY, locale='us',
    associate_tag=ASSOCIATE_TAG, cachedir='cache', cachetime=600)

# category = api.browse_node_lookup(browse_node_id='283155', response_group='TopSellers')

# product = api.item_lookup(item_id='B0051QVF7A', ResponseGroup="Accessories,\
#     BrowseNodes,EditorialReview,Images,ItemAttributes,ItemIds,Large,OfferFull,\
#     Offers,PromotionSummary,OfferSummary,Reviews,SalesRank,Similarities,Tracks")

def fetch(amazon_node_id):
    category = api.browse_node_lookup(browse_node_id=str(amazon_node_id),
        response_group='TopSellers')

    for i in category.BrowseNodes.BrowseNode.TopSellers.TopSeller:
        for j in i.ASIN:
            product = api.item_lookup(item_id=str(j), ResponseGroup="\
                EditorialReview,Images,ItemAttributes,ItemIds,OfferFull,Offers,Reviews,SalesRank")

            for p in product.Items.Item:
                print "{0}. {1} - '{2}'".format(p.SalesRank, p.ASIN, p.ItemAttributes.Title)

fetch(2956501011)
# from models import A,B,C
# p = Product()
# p.title = blablabla
# p.save()


# Kindle
# api.item_lookup('0201896842')
# The Art of Computer Programming Vol. 2

# for product in books.BrowseNodes.BrowseNode.TopItemSet.TopItem:
#     print product.ASIN
#     print product.Title
#     print product.DetailPageURL
#     print product.Author

# products = api.item_search(Keywords='kindle', search_index='All')