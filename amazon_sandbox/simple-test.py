from amazon.api import AmazonAPI
from local_settings import *


amazon = AmazonAPI(AWS_KEY, SECRET_KEY, ASSOCIATE_TAG)

product = amazon.lookup(ItemId='B009LBO334')