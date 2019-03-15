from django.contrib import admin

# Register your models here.
from .models import Movie, Festival, Screen, Screening, Place, Genre, Person, Country, Production_Company,Spoken_Language
from bifffidus.models import Tag, Crew, Cast, Job, Tag_Type, Department


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    date_hierarchy = 'release_date'
    search_fields = ['title','release_date__year']
    list_display = ('title', 'release_date', "imdb_id", "tmdb_id","original_title", "runtime")

admin.site.register(Place)
admin.site.register(Screen)
admin.site.register(Genre)

@admin.register(Festival)
class FestivalAdmin(admin.ModelAdmin):
    list_display = ('title','start_date','end_date', 'created', 'updated')

@admin.register(Screening)
class ScreeningAdmin(admin.ModelAdmin):
    date_hierarchy = 'screening_datetime'
    search_fields = ['movie__title']
    list_display = ('screening_datetime','screen','movie','festival')

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name','tmdb_id', 'profile_path')

@admin.register(Crew)
class CrewAdmin(admin.ModelAdmin):
    search_fields = ['person__name']
    list_display = ('person','job')
@admin.register(Cast)
class CastAdmin(admin.ModelAdmin):
    search_fields = ['person__name']
    list_display = ('person','character','order')
admin.site.register(Country)
admin.site.register(Production_Company)
admin.site.register(Spoken_Language)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):    
    list_display = ('name','tag_type','icon_path','hidden')

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('jobname','department')

admin.site.register(Department)

admin.site.register(Tag_Type)