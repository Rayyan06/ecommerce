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

    image_url = models.URLField(max_length=200, blank=True, null=True)
    category = models.CharField(
        max_length=2,
        choices=CATEGORIES,
    )

    def __str__(self):
        return f"{self.name}"


class Bid(models.Model):
    amount = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, related_name="bids", on_delete=models.CASCADE)

    def __str__(self):
        return f"${self.amount}"

    

class Comment(models.Model):
    text = models.CharField(max_length=64)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    

