from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit

# Image resize defaults
thumbnail_size = 200
preview_size = 1000


class Image(models.Model):
    file = models.ImageField(upload_to="images")
    data_thumbnail = ImageSpecField(source='file',
                                    processors=[ResizeToFit(width=thumbnail_size, height=thumbnail_size)],
                                    format='JPEG',
                                    options={'quality': 60})

    def __unicode__(self):
        return self.file.name
