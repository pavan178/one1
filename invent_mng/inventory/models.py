from django.db import models


# Create your models here.
class Device(models.Model):
    type = models.CharField(max_length=100, blank=False)
    price = models.IntegerField()
    choices = (
        ("AVAILABLE", "Item ready to purchase"),
        ('SOLD', 'Item sold'),
        ('Restocking', 'Item will be restocked soon')
    )
    status = models.CharField(max_length=10, choices=choices, default="SOLD")
    issues = models.CharField(max_length=100, default="No Isssues")

    class Meta:
        abstract = True

    def __str__(self):
        return 'Type : {0} Price : {1}'.format(self.type, self.price)


class Item1(Device):
    pass


class Item2(Device):
    pass


class Item3(Device):
    pass
