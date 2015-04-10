# -*- coding: utf8 -*-
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from imagegallery.models import GalleryItem, GalleryPlugin


class ImageGalleryPlugin(CMSPluginBase):
    name = u'Галерея'
    render_template = 'imagegallery/plugins/gallery.html'
    model = GalleryPlugin
    text_enabled = True

    def render(self, context, instance, placeholder):
        images = GalleryItem.objects.filter(is_active=True, gallery=instance.gallery).order_by('ord', 'id')
        context['images'] = images
        return context

plugin_pool.register_plugin(ImageGalleryPlugin)
