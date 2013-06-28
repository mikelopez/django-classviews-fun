from django.db import models

class Gallery(models.Model):
    """ Gallery table """
    name = models.CharField(max_length=30)
    category = models.ForeignKey("Category")
    gallery_location = models.TextField(blank=True, null=True)
    def save(self):
        super(Gallery, self).save()


class Category(models.Model):
    """ Category Galery table """
    name = models.CharField(max_length=30)
    description = models.TextFiel(blank=True, null=True)
    def get_galleries(self):
        return self.gallery_set.select_related()



