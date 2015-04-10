# -*- coding: utf8 -*-
from imagegallery.models import Gallery, GalleryItem
from django.contrib import admin
from ifcropper import ImageCroppingMixin


class GalleryAdmin(ImageCroppingMixin, admin.ModelAdmin):
    """ Галерея """
    list_display = ('title', '_show_galleryitems', '_short_announce', 'create_date', 'is_active')
    list_filter = ['is_active']
    date_hierarchy = 'create_date'
    search_fields = ['title', 'announce']
    readonly_fields = ['create_date']
    list_editable = ['is_active']


class GalleryItemAdmin(ImageCroppingMixin, admin.ModelAdmin):
    """ Изображение """
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

    list_display = ('title', '_show_preview', 'is_active',)
    list_filter = ['is_active']
    search_fields = ['title']
    list_editable = ['is_active']

admin.site.register(Gallery, GalleryAdmin)
admin.site.register(GalleryItem, GalleryItemAdmin)