from django.db import models
from django.utils import timezone
from datetime import date
from django.urls import reverse


#this model represent a person acting or working on a movie
class Person(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
#this model represent the job of a person on a movie (acting or working)
#    the flag is_actor is used to make difference between actor or crew
#    if flag is_actor is true, then name is the name of the character
#    if flag is_voice is true then is_actor must be true and the name is the character's voice
    
class Job(models.Model):
    name = models.CharField(max_length=200)
    is_actor = models.BooleanField
    is_voice = models.BooleanField
    def __str__(self):
        if(self.is_actor):
            return "actor - {character}".format(character=self.name)
        else:
            return self.name
        
#this model represent the credits associating a person with a job
class Credit(models.Model):
    person = models.ManyToManyField('bifffidus.Person', related_name='person', blank=True)
    job = models.ManyToManyField('bifffidus.Job', related_name='job', blank=True)
    
    def __str__(self):
        return "{job} : {person}".format(job=str(self.job), person=str(self.person))
    
class Genre(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Production_Company(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Spoken_Language(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class MovieManager(models.Manager):
    
    def create_movie(self,title,imdb_id,tmdb_id,overview,
                     runtime,tagline,backdrop_path,
                     poster_path,original_language,original_title):
        movie = self.create(title=title)        
        movie.title = title
        movie.imdb_id = imdb_id
        movie.tmdb_id = tmdb_id
        movie.overview = overview
        movie.runtime = runtime
        movie.tagline = tagline
        movie.backdrop_path = backdrop_path
        movie.poster_path = poster_path
        movie.original_language = original_language
        movie.original_title = original_title
        
        return movie

#this model represent a movie/show
class Movie(models.Model):
    title = models.CharField(max_length=250)
    imdb_id = models.CharField(max_length=200, default="")
    tmdb_id = models.CharField(max_length=200, default="")
    overview = models.TextField(default="")
    release_date = models.DateField(null=True)
    runtime = models.IntegerField(default=0)
    tagline = models.TextField(default="")
    backdrop_path = models.CharField(max_length=200,default="")
    poster_path = models.CharField(max_length=200,default="")
    original_language = models.CharField(max_length=200,default="")
    original_title = models.CharField(max_length=250,default="")
    
    #one movie can have 0..n genres, and genre can regroup 0..n movies
    genre = models.ManyToManyField('bifffidus.Genre', related_name='genre', blank=True)
    credit = models.ManyToManyField('bifffidus.Credit', related_name='credit', blank=True)
    production_company = models.ManyToManyField('bifffidus.Production_Company', related_name='production_company', blank=True)
    country = models.ManyToManyField('bifffidus.Country', related_name='country', blank=True)
    spoken_language = models.ManyToManyField('bifffidus.Spoken_Language', related_name='spoken_language', blank=True)
    #festival = models.ManyToManyField('bifffidus.Festival', related_name='festival', blank=True)
    
    objects = MovieManager()
    
    def get_absolute_url(self):            
        return reverse('movie_detail', args=[self.id])    
    
    def __str__(self):
        return self.title

class Place(models.Model):
    name = models.CharField(max_length=200)
    screen = models.ManyToManyField('bifffidus.Screen', related_name='screen_place', blank=True)
    
    def __str__(self):
        return self.name  

#this model represent each room/place where the Festival is screening the movies
# linked to Festival
class Screen(models.Model):
    #lieu, nom de la salle#
    room_name = models.CharField(max_length=200)
    #place = models.ForeignKey('bifffidus.Place', related_name='place', blank=True, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.room_name
    
#this model represent which festival (and his edition or year)
class Festival(models.Model):
    #Année, Edition, Lieu
    title = models.CharField(max_length=200, unique=True)
    start_date = models.DateField(default = timezone.now)
    end_date = models.DateField(default= timezone.now)
    place = models.ForeignKey('bifffidus.Place', related_name="place", on_delete=models.DO_NOTHING, null=True)

    def get_absolute_url(self):            
        return reverse('festival_detail', args=[self.id])  
    
    def __str__(self):
        return self.title


#this model represent when the movie has been showed 
# linked to Movie and Screen
class Screening(models.Model):
    #date, heure début, screen, movie
    screening_datetime =models.DateTimeField(default=timezone.now)
    movie = models.ForeignKey(Movie, related_name="movie", on_delete=models.SET_NULL, null=True)
    screen = models.ForeignKey(Screen, related_name="screen", on_delete=models.SET_NULL, null=True)
    festival = models.ForeignKey(Festival, related_name="festival", on_delete=models.SET_NULL, null=True)
    is_movie = models.BooleanField(default=True)
    tag = models.ManyToManyField('bifffidus.Tag', related_name='tag', blank=True)
    
    def __str__(self):
        return self.screening_datetime.strftime('%d/%m/%Y %H:%M')#+' - '+self.screen.room +')'
    
#this model represent a screening tag, it allows to categorize the screening 
# (can be for competitions, awards, special events...)    
class Tag(models.Model):
    name = models.CharField(max_length=200)    
    tag_type = models.ForeignKey('bifffidus.Tag_Type', related_name="tag_type", on_delete=models.DO_NOTHING, null=True)

#this model represent the tag type, used to categorize tags    
class Tag_Type(models.Model):
    name = models.CharField(max_length=200)