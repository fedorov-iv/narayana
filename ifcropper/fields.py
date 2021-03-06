from __future__ import unicode_literals
from django.db import models
from django import forms
from django.conf import settings
from .widgets import ImageCropWidget


class ImageCropField(models.ImageField):
    def formfield(self, **kwargs):
        defaults = {'widget': ImageCropWidget}
        defaults.update(kwargs)
        return super(ImageCropField, self).formfield(**defaults)

    def south_field_triple(self):
        """
        Return a suitable description of this field for South.
        """
        # We'll just introspect ourselves, since we inherit.
        from south.modelsinspector import introspector
        field_class = "django.db.models.fields.files.ImageField"
        args, kwargs = introspector(self)
        return (field_class, args, kwargs)


class ImageRatioField(models.CharField):
    def __init__(self, image_field, size='0x0', free_crop=False,
                 adapt_rotation=False, allow_fullsize=False, verbose_name=None,
                 help_text=None, hide_image_field=False,
                 size_warning=getattr(
                     settings, 'IMAGE_CROPPING_SIZE_WARNING', False)):
        if '__' in image_field:
            self.image_field, self.image_fk_field = image_field.split('__')
        else:
            self.image_field, self.image_fk_field = image_field, None

        self.width, self.height = list(map(int, size.split('x')))
        self.free_crop = free_crop
        self.adapt_rotation = adapt_rotation
        self.allow_fullsize = allow_fullsize
        self.size_warning = size_warning
        self.hide_image_field = hide_image_field
        field_kwargs = {
            'max_length': 255,
            'blank': True,
            'verbose_name': verbose_name,
            'help_text': help_text
        }
        super(ImageRatioField, self).__init__(**field_kwargs)

    def contribute_to_class(self, cls, name):
        super(ImageRatioField, self).contribute_to_class(cls, name)
        # attach a list of fields that are referenced by the ImageRatioField
        # so we can set the correct widget in the ModelAdmin
        if not hasattr(cls, 'crop_fields'):
            cls.add_to_class('crop_fields', {})
        cls.crop_fields[self.image_field] = {
            'fk_field': self.image_fk_field,
            'hidden': self.hide_image_field,
        }

    def formfield(self, *args, **kwargs):
        ratio = self.width / float(self.height) if not self.free_crop else 0

        kwargs['widget'] = forms.TextInput(attrs={
            'data-min-width': self.width,
            'data-min-height': self.height,
            'data-ratio': ratio,
            'data-image-field': self.image_field,
            'data-my-name': self.name,
            'data-adapt-rotation': str(self.adapt_rotation).lower(),
            'data-allow-fullsize': str(self.allow_fullsize).lower(),
            'data-size-warning': str(self.size_warning).lower(),
            'class': 'image-ratio',
        })
        return super(ImageRatioField, self).formfield(*args, **kwargs)

    def south_field_triple(self):
        """
        Return a suitable description of this field for South.
        """
        # We'll just introspect ourselves, since we inherit.
        from south.modelsinspector import introspector
        field_class = "django.db.models.fields.CharField"
        args, kwargs = introspector(self)
        return (field_class, args, kwargs)
