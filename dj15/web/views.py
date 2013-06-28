# Create your views here.
from django.views.generic import TemplateView, ListView
from models import Gallery

class AboutView(TemplateView):
    template_name = "about.html"


class GalleryView(ListView):
    model = Gallery
