from django.db import models

# Create your models here.
class Web(models.Model):
    Topic = models.CharField(max_length=264)
    AccessRecords = models.CharField(max_length=264)
    # Webpages = models.CharField(max_length=264)

    def __str__(self):
        return self.Topic

