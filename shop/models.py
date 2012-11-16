# import datetime

from django.db import models

slug_help_text = "A slug is a short label for representing a page in URL. \
Containing only letters, numbers, underscores or hyphens."

class Category(models.Model):
    """
    Here later I will add some unit testing
    """
    amazon_node_id = models.IntegerField(primary_key=True, help_text="A positive integer assigned by Amazon that uniquely identifies a product category.<br>For help refer to <a target='_blank' href='https://affiliate-program.amazon.com/gp/associates/help/t41/a6'>this page</a>.")
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
    asin = models.CharField(max_length=10, primary_key=True,
        help_text="Amazon Standard Identification Number, which is an alphanumeric token assigned by Amazon to an item that uniquely identifies it.")
    title = models.CharField(max_length=255, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.CharField(max_length=30, null=True)
    medium_image = models.CharField(max_length=255, null=True)
    large_image = models.CharField(max_length=255, null=True)
    popularity = models.IntegerField(null=True)
    manufacturer = models.CharField(max_length=255, null=True)

    def __unicode__(self):
        return self.title

class StaticPage(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=50, help_text=slug_help_text)
    text = models.TextField()
    visible = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title
