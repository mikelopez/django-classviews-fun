from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from web.views import AboutView, GalleryView, GalleryDetailView, \
        CategoryView, CategoryDetailView, CreateGallery, CreateCategory, \
        UpdateGallery, UpdateCategory, AddSomething
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
PROJECT_ROOTDIR = getattr(settings, 'PROJECT_ROOTDIR', '')

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dj15.views.home', name='home'),
    # url(r'^dj15/', include('dj15.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^about/', AboutView.as_view(), name="about-view"),

    #url(r'^dynamic/(?P<model_name>.*)/add', AddSomething.as_view(), name="dynamic-crud"),

    url(r'^gallery/add', CreateGallery.as_view(), name="galleries-add"),
    url(r'^gallery/update', UpdateGallery.as_view(), name="galleries-update"),
    url(r'^gallery/', GalleryView.as_view(), name="galleries-view"),
    url(r'^galleries/(?P<pk>\d+)/$', GalleryDetailView.as_view(), name="gallery-detail"),
    
    url(r'^categories/add', CreateCategory.as_view(), name="categories-add"),
    url(r'^categories/update', UpdateGallery.as_view(), name="categories-update"),
    url(r'^categories/', CategoryView.as_view(), name="categories-view"),
    url(r'^categories/(?P<pk>\d+)/$', CategoryDetailView.as_view(), name="category-detail"),


    #(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':'%s/static/' % (PROJECT_ROOTDIR), 'show_indexes': True}),


)
