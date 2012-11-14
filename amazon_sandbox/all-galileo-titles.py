"""
Get all books published by "Galileo Press".
"""

import caching
from local_settings import *

api = caching.ResponseCachingAPI(AWS_KEY, SECRET_KEY, locale='us',
    associate_tag=ASSOCIATE_TAG, cachedir='.', cachetime=600)

for root in api.item_search('Books', BrowseNode=283155, ResponseGroup='Large'):

    # extract paging information
    total_results = root.Items.TotalResults.pyval
    total_pages = root.Items.TotalPages.pyval
    try:
        current_page = root.Items.Request.ItemSearchRequest.ItemPage.pyval
    except AttributeError:
        current_page = 1
        
    print 'page %d of %d' % (current_page, total_pages)
    
    #~ from lxml import etree
    #~ print etree.tostring(root, pretty_print=True)
    
    nspace = root.nsmap.get(None, '')
    books = root.xpath('//aws:Items/aws:Item', 
                         namespaces={'aws' : nspace})
    
    for book in books:
        print unicode(book.ASIN),
        print unicode(book.ItemAttributes.Author), ':', 
        print unicode(book.ItemAttributes.Title),
        if hasattr(book.ItemAttributes, 'ListPrice'): 
            print unicode(book.ItemAttributes.ListPrice.FormattedPrice)
        elif hasattr(book.OfferSummary, 'LowestUsedPrice'):
            print u'(used from %s)' % book.OfferSummary.LowestUsedPrice.FormattedPrice
