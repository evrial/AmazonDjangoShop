"""
Get all books published by "Galileo Press".
"""

from settings import AWS_KEY, SECRET_KEY, ASSOCIATE_TAG
from amazonproduct.api import API

if __name__ == '__main__':
    
    api = API(AWS_KEY, SECRET_KEY, 'us', ASSOCIATE_TAG)
    
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
