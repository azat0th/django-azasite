from django.contrib import admin

# Register your models here.
from .models import Movie, Festival, Screen, Screening, Place, Genre, Job, Person, Country, Production_Company,Spoken_Language, Credit

admin.site.register(Movie)
admin.site.register(Place)
admin.site.register(Festival)
admin.site.register(Screen)
admin.site.register(Screening)
admin.site.register(Genre)
admin.site.register(Job)
admin.site.register(Person)
admin.site.register(Credit)
admin.site.register(Country)
admin.site.register(Production_Company)
admin.site.register(Spoken_Language)