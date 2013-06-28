# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from models import Gallery, Category
from forms import GalleryForm

class AboutView(TemplateView):
    """ About Page View """
    template_name = "about.html"


class GalleryView(ListView):
    """ Gallery List Page View """
    model = Gallery

class CreateGallery(CreateView):
    """ Create Gallery page view """
    model = Gallery

class GalleryDetailView(DetailView):
    """ Gallery Detail Page View """
    queryset = Gallery.objects.all()
    def get_object(self):
        # do anything anytime an object is accessed
        object = super(GalleryDetailView, self).get_object()
        # anything after here
        return object


class CategoryView(ListView):
    """ Category List Page view """
    model = Category

class CreateCategory(CreateView):
    """ Create Category page view """
    model = Category

class CategoryDetailView(DetailView):
    """ Category Detail Page View """
    queryset = Category.objects.all()




