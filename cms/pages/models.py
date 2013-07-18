from django.db import models
from django.core.urlresolvers import reverse

class Page(models.Model):
    title           = models.CharField( max_length=500, help_text="Page Title" )
    body            = models.TextField( help_text="Page Body" )
    picture         = models.ImageField( upload_to="photos/" )
    timestamp       = models.DateTimeField( auto_now_add=True, editable=False ) 

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('page-detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-timestamp']



