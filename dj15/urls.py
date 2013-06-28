from django.conf.urls import patterns, include, url
from web.views import AboutView, GalleryView, GalleryDetailView, \
        CategoryView, CategoryDetailView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dj15.views.home', name='home'),
    # url(r'^dj15/', include('dj15.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^about/', AboutView.as_view(), name="about-view"),

    url(r'^gallery/', GalleryView.as_view(), name="galleries-view"),
    url(r'^categories/', CategoryView.as_view(), name="categories-view"),

    url(r'^galleries/(?P<pk>\d+)/$', GalleryDetailView.as_view(), name="gallery-detail"),
    url(r'^categories/(?P<pk>\d+)/$', CategoryDetailView.as_view(), name="category-detail"),

)
