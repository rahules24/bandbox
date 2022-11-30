from django.db import models
from django.utils.timezone import now


class Item(models.Model):
    item_id = models.AutoField
    item_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    price_press = models.IntegerField(default=0)
    image = models.ImageField(upload_to="images", default="")

    def __str__(self):
        return self.item_name


class Slip(models.Model):
    # items = ['BABY COAT', 'BLANKET I', 'BLANKET I - II PLY', 'BLANKET II', 'BLANKET II - II PLY', 'CARPET', 'COAT', 'CURTAIN', 'GOWN', 'HALF JACKET', 'JACKET', 'LADIES SHIRT', 'LADIES SUIT', 'LEHENGA', 'OUILT I', 'PANT', 'QUILT II', 'SAREE', 'SHAWL', 'SHIRT', 'SUIT 2', 'SUIT 3', 'SWEATER', 'WAISTCOAT']
    slip_id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=500)
    phone = models.IntegerField(blank=True, null=True)
    date = models.DateField(default=now)
    due_date = models.DateField()
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField(default=0)
    # item = models.CharField(max_length=50, choices=[(item, item) for item in items])

    def __str__(self):
        return self.address
