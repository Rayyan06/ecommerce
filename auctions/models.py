from django.contrib.auth.models import AbstractUser
from django.db import models


        
CATEGORIES = [
    ('FA', 'Fashion'),
    ('TO', 'Toys'),
    ('EL', 'Electronics'),
    ('HO', 'Home')
]

class User(AbstractUser):
    watchlist = models.ManyToManyField("Listing", blank=True)



class Listing(models.Model):


    name = models.CharField(max_length=64)
    is_active = models.BooleanField(default=True)
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

    def get_greatest_bid(self):

        return self.bids.order_by('-amount').first() 

    
    @property
    def price(self):
        if self.get_greatest_bid():
            return self.get_greatest_bid().amount
        else:
            return self.starting_bid






class Bid(models.Model):
    amount = models.DecimalField(decimal_places=2, max_digits=4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, related_name="bids", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.amount}"

    

class Comment(models.Model):
    title = models.CharField(max_length=20)
    text = models.CharField(max_length=64)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
    

    

