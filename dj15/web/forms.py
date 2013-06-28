from django import forms

class GalleryForm(forms.Form):
    """ Form for Gallery model """
    name = forms.CharField()
    location = forms.CharField(widget=forms.Textarea)


class CategoryForm(forms.Form):
    """ Forms for Category model """
    name = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
