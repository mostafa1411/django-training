from django import forms
from .models import Artist


class ArtistFrom(forms.ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'
