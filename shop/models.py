import datetime

from django.db import models

class Category(models.Model):
    """
    Here later I will add some unit testing
    """
    active = models.BooleanField(default=True)
    amazon_node_id = models.IntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True,
        default=datetime.datetime.now())
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

class Product(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    popularity = models.IntegerField()

    def __unicode__(self):
        return self.title
