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


class BidForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.listing_id = kwargs.pop("listing_id")
        super(BidForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Bid
        fields = ['amount']
        widgets={
            'amount': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Bid Amount',
                }
            ),
        }
    
    def clean_amount(self):
        amount = self.cleaned_data['amount']
        listing = Listing.objects.get(pk=self.listing_id)
        if amount < listing.price:
            raise forms.ValidationError(
                "Please bid more than the highest bid $%(value)s", 
                params={'value': listing.price},
                code="invalid")

        # Always return the modified field
        return amount


    

        
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [ 'title','text']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mb-1', 'placeholder': 'Title'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Comment Text'}),

        }


 