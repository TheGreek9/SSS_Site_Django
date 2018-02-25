from django.db import models
from django.urls import reverse

# Create your models here.

class Song(models.Model):

    user = models.OneToOneField('User', on_delete=models.CASCADE)
    song_title = models.TextField()
    singer = models.TextField()
    artist = models.TextField()
    genre = models.TextField(blank=True)
    original_musical = models.TextField(blank=True)
    musicalNon = models.CharField(max_length=12)
    sheet_music = models.URLField(blank=True)
    spotify_id = models.TextField(blank=True)
    spotify_preview = models.URLField(blank=True)
    pendingNon = models.CharField(max_length=12)
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
         """
         Returns the url to access a particular instance of MyModelName.
         """
         return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.field_name

class Musical(models.Model):

    user = models.OneToOneField('User', on_delete=models.CASCADE)
    musical_title = models.TextField()
    playwright = models.TextField()
    composer = models.TextField()
    lyricist = models.TextField(blank=True)
    genre = models.TextField(blank=True)
    production_year = models.TextField(blank=True)
    plot = models.TextField()
    pendingNon = models.CharField(max_length=12)
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
         """
         Returns the url to access a particular instance of MyModelName.
         """
         return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.field_name

class Role(models.Model):

    user = models.OneToOneField('User', on_delete=models.CASCADE)
    song = models.ManyToManyField('Song')
    musical = models.ForeignKey('Musical', on_delete=models.CASCADE)
    role = models.TextField()
    pendingNon = models.CharField(max_length=12)
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
         """
         Returns the url to access a particular instance of MyModelName.
         """
         return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.field_name

class User(models.Model):

    name = models.TextField()
    user_email = models.EmailField()
    password = models.TextField()

    def get_absolute_url(self):
         """
         Returns the url to access a particular instance of MyModelName.
         """
         return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.field_name
