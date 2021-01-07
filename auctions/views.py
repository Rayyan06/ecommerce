from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


from .models import User, Listing
from .forms import ListingForm

def index(request):
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all()
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
    form = ListingForm(initial={'listed_by': request.user})
    if request.method=='POST':
        form = ListingForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect((reverse("index")))
        
    return render(request, "auctions/create.html", {
        "form": form,
    })

def listing(request, listing_id):
    return render(request, "auctions/listing.html", {
        "listing": Listing.objects.get(pk=listing_id)
    })



def watchlist(request):
    return render(request, "auctions/watchlist.html", {
        "watchlist": request.user.watchlist.all()
    })
# Add and Remove from watchlist views
def add_to_watchlist(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    if request.user.watchlist:
        request.user.watchlist.add(listing)

    return HttpResponseRedirect(reverse("watchlist"))

def remove_from_watchlist(request, listing_id):
    listing = Listing.objects.get(listing_id)
    request.user.watchlist.remove(listing)