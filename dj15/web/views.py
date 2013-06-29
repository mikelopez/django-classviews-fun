# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from django.shortcuts import render
from models import Gallery, Category
from forms import GalleryForm, CategoryForm


class AboutView(TemplateView):
    """ About Page View """
    template_name = "about.html"

class GalleryView(ListView):
    """ Gallery List Page View """
    model = Gallery

class CreateGallery(CreateView):
    """ Create Gallery page view """
    model = Gallery

class UpdateGallery(UpdateView):
    """ Update view """
    model = Gallery
    
class GalleryDetailView(DetailView):
    """ Gallery Detail Page View """
    queryset = Gallery.objects.all()
    def get_object(self, **kwargs):
        object = super(GalleryDetailView, self).get_object(**kwargs)
        return object



class CategoryView(ListView):
    """ Category List Page view """
    model = Category

class CreateCategory(CreateView):
    """ Create Category page view """
    model = Category

class UpdateCategory(UpdateView):
    """ Update category view """
    model = Gallery

class CategoryDetailView(DetailView):
    """ Category Detail Page View """
    queryset = Category.objects.all()
    def get_object(self, **kwargs):
        object = super(GalleryDetailView, self).get_object(**kwargs)
        return object



