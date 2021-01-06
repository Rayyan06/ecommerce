from .models import Listing
from django import forms

class ListingForm(forms.ModelForm):
   
    class Meta:
        model = Listing
        fields=['name', 'description', 'starting_bid', 'image_url', 'category', 'listed_by']
        widgets = {
            'listed_by': forms.HiddenInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'starting_bid': forms.NumberInput(attrs={'class':'form-control'}),
            'image_url': forms.URLInput(attrs={'class': 'form-control'}),
            'category': forms.

        }

