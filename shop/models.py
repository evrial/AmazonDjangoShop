import datetime

from django.db import models

slug_help_text = "A slug is a short label for representing a page in URL. \
Containing only letters, numbers, underscores or hyphens."

# todo: abstract class (title, visible, created, modified)
class Category(models.Model):
    """
    Here later I will add some unit testing
    """
    amazon_node_id = models.IntegerField(
        help_text="For help refer to <a target='_blank' href='https://affiliate-program.amazon.com/gp/associates/help/t41/a6'>this page</a>.")
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=50, help_text=slug_help_text)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True,
        default=datetime.datetime.now())
    modified = models.DateTimeField(auto_now=True)
    visible = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title

class Product(models.Model):
    category = models.ForeignKey(Category)
    asin = models.CharField(max_length=10,
        help_text="For info about ASIN please refer to <a target='_blank' href='http://en.wikipedia.org/wiki/ASIN'>this page</a>.")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    popularity = models.IntegerField()

    def __unicode__(self):
        return self.title

class StaticPage(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=50, help_text=slug_help_text)
    text = models.TextField()
    visible = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title
