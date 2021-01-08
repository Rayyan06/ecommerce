from .models import Listing, Bid, Comment
from django import forms

class ListingForm(forms.ModelForm):
    listed_by = forms.CharField(required=False)

    class Meta:
        model = Listing
        fields=['name', 'description', 'starting_bid', 'image_url', 'category']
        widgets = {
            'listed_by': forms.HiddenInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'starting_bid': forms.NumberInput(attrs={'class':'form-control'}),
            'image_url': forms.URLInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class':'form-control'})

        }


class BidForm(forms.Form):

    amount = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Bid Amount'
            }
        ))


    def __init__(self, *args, **kwargs):
        """
        Override the __init__ method so we can have access
        to request.user and listing_id for validation
        """
        self.request_user = kwargs.pop("request_user")
        self.listing = kwargs.pop("listing")
        super(BidForm, self).__init__(*args, **kwargs)
    
    def clean_amount(self):

        amount = self.cleaned_data["amount"]

        if self.listing.price > amount:
            raise forms.ValidationError(f"Please bid higher than the current bid (${self.listing.price})")
        
        return amount
        

        
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [ 'title','text']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mb-1', 'placeholder': 'Title'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Comment Text'}),

        }


 