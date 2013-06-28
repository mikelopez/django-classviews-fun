# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView
from models import Gallery, Category

class AboutView(TemplateView):
    """ About Page View """
    template_name = "about.html"

class GalleryView(ListView):
    """ Gallery List Page View """
    model = Gallery

class CategoryView(ListView):
    """ Category List Page view """
    model = Category

class GalleryDetailView(DetailView):
    """ Gallery Detail Page View """
    queryset = Gallery.objects.all()
    def get_object(self):
        # do anything anytime an object is accessed
        object = super(GalleryDetailView, self).get_object()
        # anything after here
        return object

class CategoryDetailView(DetailView):
    """ Category Detail Page View """
    queryset = Category.objects.all()



