from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("categories", views.categories, name="categories"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("listing/<int:listing_id>", views.listing, name="listing"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("add-to-watchlist/<int:listing_id>", views.add_to_watchlist, name="add_to_watchlist"),
    path("remove-from-watchlist/<int:listing_id>", views.remove_from_watchlist, name="remove_from_watchlist"),
    path("close-auction/<int:listing_id>", views.close_auction, name="close_auction"),
    path("comment/<int:listing_id>/", views.comment, name="comment"),
    path("categories/<str:category_str>", views.category, name="category")
]
