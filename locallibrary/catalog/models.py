from django.db import models

# Create your models here.
class Genre(models.Model):

    """ Model representing a book genre."""
    
    name = models.CharField(max_length=30, help_text='Enter a book genre (e.g. Science Fiction)')

  
    def __str__(self):
        return self.name

