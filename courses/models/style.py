from django.db import models
from django.db.models import SET_NULL
from djangocms_text_ckeditor.fields import HTMLField
from parler.models import TranslatableModel, TranslatedFields


class Style(TranslatableModel):
    name = models.CharField(max_length=30, unique=True, blank=False)
    parent_style = models.ForeignKey(to="Style", null=True, blank=True, related_name='children', on_delete=SET_NULL)
    filter_enabled = models.BooleanField(default=False, null=False, blank=False)
    filter_enabled.help_text = 'If set to true, users can filter courses list based on this style'
    url_info = models.URLField(max_length=500, blank=True, null=True)
    url_info.help_text = "A url to an information page (e.g. Wikipedia)."
    url_video = models.URLField(max_length=500, blank=True, null=True)
    url_video.help_text = "A url to a demo video (e.g Youtube)."
    url_playlist = models.URLField(max_length=500, blank=True, null=True)
    url_playlist.help_text = "A url to a playlist (e.g on online-Spotify, Youtube)."

    translations = TranslatedFields(
        description=HTMLField(verbose_name='[TR] Description', blank=True, null=True)
    )


    def has_external_urls(self):
        return self.url_info or self.url_video or self.url_playlist

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        ordering = ['name']

    def is_child_of(self, style):
        current_style = self
        while current_style is not None:
            current_style = current_style.parent_style
            if current_style == style:
                return True

        return False
