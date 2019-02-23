from django.contrib import admin

# Register your models here.
from .models import Movie, Festival, Screen, Screening, Place, Genre, Person, Country, Production_Company,Spoken_Language
from bifffidus.models import Tag_Movie_Festival, Tag, Crew, Cast, Job, Tag_Type

admin.site.register(Movie)
admin.site.register(Place)
admin.site.register(Festival)
admin.site.register(Screen)
admin.site.register(Screening)
admin.site.register(Genre)
admin.site.register(Person)
admin.site.register(Crew)
admin.site.register(Cast)
admin.site.register(Country)
admin.site.register(Production_Company)
admin.site.register(Spoken_Language)
admin.site.register(Tag)
admin.site.register(Tag_Movie_Festival)
admin.site.register(Job)
admin.site.register(Tag_Type)