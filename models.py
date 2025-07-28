from django.db import models

class Movie(models.Model):
    STATUS_CHOICES = [
        ('seen', 'Film i shikuar'),
        ('unseen', 'Për t’u shikuar'),
    ]

    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    year = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    poster_url = models.URLField(blank=True, null=True)  
    shikuar_me = models.CharField(max_length=255, blank=True, null=True)
    pershkrim = models.TextField(blank=True, null=True)  
    

    def __str__(self):
        return self.title


