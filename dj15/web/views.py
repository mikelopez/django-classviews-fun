# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
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
    form_class = GalleryForm
    def post(request, *args, **kwargs):
        print request
        print args
        print kwargs

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

class UpdateCategory(UpdateView):
    """ Update category view """
    form_class = CategoryForm
    def post(request, *args, **kwargs):
        print request
        print args

class CategoryDetailView(DetailView):
    """ Category Detail Page View """
    queryset = Category.objects.all()




