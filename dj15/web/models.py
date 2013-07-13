from django.db import models
from django.core.urlresolvers import reverse

class Gallery(models.Model):
    """ Gallery table """
    name = models.CharField(max_length=30)
    category = models.ForeignKey("Category")
    gallery_location = models.TextField(blank=True, null=True)
    def get_absolute_url(self):
        return reverse('gallery-detail', kwargs={'pk': self.pk})

class Category(models.Model):
    """ Category Galery table """
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return str(self.name)
    def __unicode__(self):
        return unicode(self.name)
    def get_galleries(self):
        return self.gallery_set.select_related()
    def get_absolute_url(self):
        return reverse('category-detail', kwargs={'pk': self.pk})



