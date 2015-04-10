from django import template
from imagegallery.models import Gallery
import re

register = template.Library()


@register.simple_tag
def get_gallery(gallery_id):
   return Gallery.objects.get(pk=gallery_id).title