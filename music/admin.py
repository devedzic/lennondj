from django.contrib import admin

# Register your models here.
# Each model should be registered using: admin.site.register(<Model>)
from music.models import Band, Musician

admin.site.register(Band)
admin.site.register(Musician)


