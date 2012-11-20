# import datetime

from django.db import models

slug_help_text = "A slug is a short label for representing a page in URL. \
Containing only letters, numbers, underscores or hyphens."

class Category(models.Model):
    """
    Here later I will add some unit testing
    """
    SEARCH_INDEXES = (
        (0, u'Apparel'),
        (1, u'Appliances'),
        (2, u'ArtsAndCrafts'),
        (3, u'Automotive'),
        (4, u'Baby'),
        (5, u'Beauty'),
        (6, u'Blended'),
        (7, u'Books'),
        (8, u'Classical'),
        (9, u'Collectibles'),
        (10, u'DVD'),
        (11, u'DigitalMusic'),
        (12, u'Electronics'),
        (13, u'GiftCards'),
        (14, u'GourmetFood'),
        (15, u'Grocery'),
        (16, u'HealthPersonalCare'),
        (17, u'HomeGarden'),
        (18, u'Industrial'),
        (19, u'Jewelry'),
        (20, u'KindleStore'),
        (21, u'Kitchen'),
        (22, u'LawnAndGarden'),
        (23, u'Marketplace'),
        (24, u'MP3Downloads'),
        (25, u'Magazines'),
        (26, u'Miscellaneous'),
        (27, u'Music'),
        (28, u'MusicTracks'),
        (29, u'MusicalInstruments'),
        (30, u'MobileApps'),
        (31, u'OfficeProducts'),
        (32, u'OutdoorLiving'),
        (33, u'PCHardware'),
        (34, u'PetSupplies'),
        (35, u'Photo'),
        (36, u'Shoes'),
        (37, u'Software'),
        (38, u'SportingGoods'),
        (39, u'Tools'),
        (40, u'Toys'),
        (41, u'UnboxVideo'),
        (42, u'VHS'),
        (43, u'Video'),
        (44, u'VideoGames'),
        (45, u'Watches'),
        (46, u'Wireless'),
        (47, u'WirelessAccessories'),
        )
    amazon_node_id = models.IntegerField(primary_key=True, help_text="A positive integer assigned by Amazon that uniquely identifies a product category.<br>For help refer to <a target='_blank' href='https://affiliate-program.amazon.com/gp/associates/help/t41/a6'>this page</a>.")
    search_index = models.IntegerField(choices=SEARCH_INDEXES)
    title = models.CharField(max_length=255, null=True)
    slug = models.SlugField(max_length=50, null=True, help_text=slug_help_text)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    visible = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title

class Product(models.Model):
    category = models.ForeignKey(Category)
    detailpageurl = models.TextField(blank=True, null=True)
    asin = models.CharField(max_length=10, primary_key=True,
        help_text="Amazon Standard Identification Number, which is an alphanumeric token assigned by Amazon to an item that uniquely identifies it.")
    title = models.CharField(max_length=255, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.CharField(max_length=30, null=True)
    publisher = models.CharField(max_length=255, null=True)
    manufacturer = models.CharField(max_length=255, null=True)
    brand = models.CharField(max_length=255, null=True)
    medium_image = models.CharField(max_length=255, null=True)
    large_image = models.CharField(max_length=255, null=True)
    popularity = models.IntegerField(null=True)

    def __unicode__(self):
        return self.title

class StaticPage(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=50, help_text=slug_help_text)
    text = models.TextField()
    visible = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title
