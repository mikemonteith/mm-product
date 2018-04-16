from django.db import models
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from mm_core.core.models import CorePage

class MikesPage(CorePage):
    old_url = models.CharField(max_length=1024, blank=True)

    content_panels = CorePage.content_panels + [
        FieldPanel('old_url'),
    ]
