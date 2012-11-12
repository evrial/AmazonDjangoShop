# from amazonproduct import API
import caching
from local_settings import *


api = caching.ResponseCachingAPI(AWS_KEY, SECRET_KEY, 'us', ASSOCIATE_TAG, 'temp')

books = api.browse_node_lookup('283155', 'TopSellers')
# api.item_lookup('0201896834')
# The Art of Computer Programming Vol. 1
# api.item_lookup('0201896842')
# The Art of Computer Programming Vol. 2