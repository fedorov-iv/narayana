from django.conf.urls import patterns, include, url
#from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.contrib import admin
from cms.sitemaps import CMSSitemap
from django.utils.functional import curry
from django.views.defaults import server_error, page_not_found, permission_denied
from django.conf.urls.static import static

admin.autodiscover()

handler500 = curry(server_error, template_name='500.html')
handler404 = curry(page_not_found, template_name='404.html')
handler403 = curry(permission_denied, template_name='403.html')

urlpatterns = patterns('',
                       #url(r'^captcha/', include('captcha.urls')),
                       url(r'^tinymce/', include('tinymce.urls')),
                       url(r'^mce_filebrowser/', include('mce_filebrowser.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
                           {'sitemaps': {'cmspages': CMSSitemap}}),
                       url(r'^', include('cms.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
