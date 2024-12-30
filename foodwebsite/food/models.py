from django.db import models

class Item(models.Model):

    def __str__(self):
        return self.item_name
    
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default="https://s3-figma-hubfile-images-production.figma.com/hub/file/carousel/img/c03d315e1938db5a050bd6edd265cdcb5787dd24")
