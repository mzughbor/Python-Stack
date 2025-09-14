# TVShows/forms.py
from django import forms
from .models import TVShow

class TVShowForm(forms.ModelForm):
    class Meta:
        model = TVShow
        fields = ["title", "network", "release_date", "desc"]

    def clean_title(self):
        title = self.cleaned_data.get("title")
        # When updating, instance.pk will be set, so exclude it
        qs = TVShow.objects.filter(title__iexact=title)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("A TV show with this title already exists.")
        return title
