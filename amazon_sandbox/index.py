# amazon simple product advertising api
from amazon.api import AmazonAPI
from local_settings import *

amazon = AmazonAPI(AWS_KEY, SECRET_KEY, ASSOCIATE_TAG, 'US')
product = amazon.lookup(ItemId='B0051QVF7A')

products = amazon.search(Keywords='kindle', SearchIndex='All')

for i, p in enumerate(products):
    print "{0}. '{1}'".format(i, p.title)
