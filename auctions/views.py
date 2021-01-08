from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


from .models import User, Listing, Bid
from .forms import ListingForm, BidForm, CommentForm

def index(request):
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.filter(is_active=True)
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")



@login_required
def create(request):
    
    if request.method=='POST':
        form = ListingForm(request.POST, initial={'listed_by': request.user})

        if form.is_valid():
            f = form.save(commit=False)
            f.listed_by = request.user
            f.save()

            return HttpResponseRedirect((reverse("listing", args=[f.id])))
        else:
            print(form.errors)

    else:
        form = ListingForm(initial={'listed_by': request.user})
        
    
    return render(request, "auctions/create.html", {
        "form": form,
    })

def listing(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)

    if request.method=='POST':
        bid_form = BidForm(request.POST, request_user=request.user, listing=listing)
        comment_form = CommentForm()

        if bid_form.is_valid():
            amount = bid_form.cleaned_data["amount"]

            Bid.objects.create(user=request.user, amount=amount, listing=listing)
        


   
        
    else:
        bid_form = BidForm(request_user=request.user, listing=listing)
        comment_form = CommentForm()

    listing_in_watchlist = False
    is_creator = (request.user == listing.listed_by)

    if request.user.is_authenticated and listing in request.user.watchlist.all():
        listing_in_watchlist = True

    if not listing.is_active:
        highest_bid = listing.get_greatest_bid()
        if request.user == highest_bid.user:
            messages.add_message(request, messages.INFO, f"Congratulations, you have won this auction!")
        else:
            if is_creator:
                messages.add_message(request, messages.INFO, f"You have closed this listing. The winner was <strong>{highest_bid.user}</strong>.")
            else:
                messages.add_message(request, messages.INFO, f"Oh no, you lost this listing! Better luck next time...")

            

    return render(request, "auctions/listing.html", {
        "listing": listing,
        "listing_in_watchlist": listing_in_watchlist,
        "is_creator": is_creator,
        "comment_form": comment_form,
        "bid_form": bid_form, 
        
    })


@login_required
def watchlist(request):
    return render(request, "auctions/watchlist.html", {
        "watchlist": request.user.watchlist.all()
    })

# Add and Remove from watchlist views
@login_required
def add_to_watchlist(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    if request.user.watchlist:
        request.user.watchlist.add(listing)

    return HttpResponseRedirect(reverse("listing", args=[listing_id]))

@login_required
def remove_from_watchlist(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    request.user.watchlist.remove(listing)

    return HttpResponseRedirect(reverse("watchlist"))



@login_required
def close_auction(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)

    listing.is_active = False
    listing.save()

    return HttpResponseRedirect(reverse("listing", args=[listing_id]))
    



@login_required
def comment(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)

    comment_form = CommentForm(request.POST)

    if comment_form.is_valid():
                
        comment = comment_form.save(commit=False)
        comment.user = request.user
        comment.listing = Listing.objects.get(pk=listing_id)
        comment.save()


    return HttpResponseRedirect(reverse('listing', args=[listing_id]))

   
