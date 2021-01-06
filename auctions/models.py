from django.contrib.auth.models import AbstractUser
from django.db import models

CATEGORIES = [
    ('FA', 'Fashion'),
    ('TO', 'Toys'),
    ('EL', 'Electronics'),
    ('HO', 'Home')
]

class User(AbstractUser):
    pass



class Listing(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    listed_by = models.ForeignKey(User, on_delete=models.CASCADE)
    starting_bid = models.IntegerField()
    category = models.CharField(
        max_length=2,
        choices=CATEGORIES,
    )


class Bid(models.Model):
    amount = models.IntegerField()
    listing = models.ForeignKey(Listing, related_name="bids", on_delete=models.CASCADE)

class Comment(models.Model):
    text = models.CharField(max_length=64)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

