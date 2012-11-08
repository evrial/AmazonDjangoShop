from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models
    description = models.TextField()
    amazon_id = models.IntegerField()
    pub_date = models.DateTimeField('date added')

    def __unicode__(self):
        return self.title

class Product(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    popularity = models.IntegerField()

    def __unicode__(self):
        return self.title