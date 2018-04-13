from wagtail.wagtailcore.models import Page

from django.db import models
from wagtail.wagtailadmin.edit_handlers import FieldPanel


class MikesPage(Page):
    old_url = models.CharField(max_length=1024, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('old_url'),
    ]
