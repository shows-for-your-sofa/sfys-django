from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=250, blank=True)
    email_address = models.CharField(max_length=50, blank=True) # Scrapers may not find this information, but we'll require it at the form level
    email_verified = models.BooleanField(default=False)


class Genre(models.Model):
    genre = models.CharField(max_length=50) # E.g., classical, folk, jazz, popular, spoken word, dance, misc


class Event(models.Model):
    date = models.DateField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField() # Scrapers will use start_time + 1 hour as the default
    name = models.CharField(max_length=50)
    event_link = models.CharField(max_length=250)
    contribution_link = models.CharField(max_length=250, blank=True) # Do not use null=True: https://docs.djangoproject.com/en/3.0/ref/models/fields/#null
    description = models.CharField(max_length=500, blank=True) # CharField enforces max_length at the database level, whereas TextField does not
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, blank=True, null=True, on_delete=models.CASCADE)

