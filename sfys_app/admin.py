from django.contrib import admin

from .models import Artist, Event, Genre

admin.site.register(Artist)
admin.site.register(Genre)
admin.site.register(Event)
