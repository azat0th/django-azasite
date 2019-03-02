from django.db import models
from django.utils import timezone
from datetime import date
from django.urls import reverse


#this model represent a person acting or working on a movie
class Person(models.Model):
    name = models.CharField(max_length=200, default="")
    tmdb_id = models.IntegerField(default=0)
    profile_path = models.CharField(max_length=200,default="")
    gender = models.IntegerField(default=0)   
    #imdb_id = models.CharField(max_length=50, null=True)
    #birthday = models.DateField(null=True)
    #deathday= models.DateField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
        
    def getGender(self):
        if(self.gender==0):
            return "Unknown"
        if(self.gender==1):
            return "Female"
        if(self.gender==2):
            return "Male"
        
    def __str__(self):
        return "{name}".format(name=self.name, tmdb_id=self.tmdb_id, gender=self.getGender(), profile_path=self.profile_path, pk=self.pk)
    
#this model represent the job of a person on a movie (acting or working)
#    the flag is_actor is used to make difference between actor or crew
#    if flag is_actor is true, then name is the name of the character
#    if flag is_voice is true then is_actor must be true and the name is the character's voice
    
    
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

'''class MovieManager(models.Manager):
    
    def create_movie(self,title,imdb_id,tmdb_id,overview,
                     runtime,tagline,backdrop_path,
                     poster_path,original_language,original_title,
                     release_date):
        movie = self.create(title=title)        
        #movie.title = title
        movie.imdb_id = imdb_id
        movie.tmdb_id = tmdb_id
        movie.overview = overview
        movie.runtime = runtime
        movie.tagline = tagline
        movie.backdrop_path = backdrop_path
        movie.poster_path = poster_path
        movie.original_language = original_language
        movie.original_title = original_title
        if(release_date != 0):
            movie.release_date = release_date
        
        return movie'''

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
    genre = models.ManyToManyField('bifffidus.Genre', related_name='movie_genre', blank=True)
    cast = models.ManyToManyField('bifffidus.Cast', related_name='movie_cast', blank=True)
    crew = models.ManyToManyField('bifffidus.Crew', related_name='movie_crew', blank=True)
    production_company = models.ManyToManyField('bifffidus.Production_Company', related_name='production_company', blank=True)
    country = models.ManyToManyField('bifffidus.Country', related_name='country', blank=True)
    spoken_language = models.ManyToManyField('bifffidus.Spoken_Language', related_name='spoken_language', blank=True)
    #festival = models.ManyToManyField('bifffidus.Festival', related_name='festival', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    '''objects = MovieManager()'''
        
    def get_poster_image_url_185(self):
        url = "/static/img/movie.no-img.185.png"
        if(self.poster_path and self.poster_path!="None"):
            url_img="https://image.tmdb.org/t/p/w185"
            url = url_img + self.poster_path
        return url
                
    def get_poster_image_url_45(self):
        url = "/static/img/movie.no-img.45.png"
        if(self.poster_path and self.poster_path!="None"):
            url_img="https://image.tmdb.org/t/p/w45"
            url = url_img + self.poster_path
        return url
    
    def get_poster_image_url_92(self):
        url = "/static/img/movie.no-img.92.png"
        if(self.poster_path and self.poster_path!="None"):
            url_img="https://image.tmdb.org/t/p/w92"
            url = url_img + self.poster_path
        return url
    def get_absolute_url(self):            
        return reverse('movie_detail', args=[self.id])    
    
    def __str__(self):
        return self.title
    
class Job(models.Model):
    department = models.CharField(max_length=200, default="unknown")
    jobname = models.CharField(max_length=200, default="unknown")
    def __str__(self):        
        return "{job} : {department}".format(department=self.department,job=self.jobname)
    
    
class Crew(models.Model):
    job = models.ForeignKey('bifffidus.Job', related_name='job_person', on_delete=models.CASCADE, null=False)
    person = models.ForeignKey('bifffidus.Person', related_name='crew_person', on_delete=models.CASCADE, null=True)
    #movie = models.ForeignKey(Movie, related_name="movie_crew", on_delete=models.CASCADE, null=True)    
    
    def __str__(self):        
        return "{department} : {job} : {person}".format(department=self.job.department,job=self.job.jobname, person=self.person)
    
class Cast(models.Model):
    order = models.IntegerField(default=0)
    character= models.CharField(max_length=100, default="")
    person = models.ForeignKey('bifffidus.Person', related_name='cast_person', on_delete=models.CASCADE, null=True)    
    #movie = models.ForeignKey(Movie, related_name="movie_cast", on_delete=models.CASCADE, null=True)    
    
    def __str__(self):        
        return "{character} [{order}]: {person}".format(character=self.character,order=self.order, person=self.person)

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
    place = models.ManyToManyField('bifffidus.Place', related_name="place", blank=True)
    
    poster_path = models.CharField(max_length=200, default='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def get_poster_image_url(self):
        url = ""
        if(self.poster_path):            
            url = "/static/img/" + self.poster_path
        return url
    
    def get_absolute_url(self):            
        return reverse('festival_detail', args=[self.id])  
    
    def __str__(self):
        return self.title

class ScreeningQuerySet(models.QuerySet):
    def by_day(self):        
        return self
    
class ScreeningManager(models.Manager):
    
    def by_day(self):
        screenings_set = self.get_queryset().by_day()
        return screenings_set
     
class Tag_Type(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
#this model represent a screening tag, it allows to categorize the screening 
# (can be for competitions, awards, special events...)    
class Tag(models.Model):
    name = models.CharField(max_length=200)  
    tag_type = models.ForeignKey(Tag_Type, related_name="tag_type", on_delete=models.CASCADE, null=True)
    icon_path = models.CharField(max_length=200, default='', blank=True)
    
    def check_type(self):
        if(self.tag_type.id != 3):
            return True
        else:
            return False
        
    def __str__(self):
        return self.name        
#this model represent when the movie has been showed 
# linked to Movie and Screen
class Screening(models.Model):
    #date, heure début, screen, movie
    screening_datetime =models.DateTimeField(default=timezone.now)
    movie = models.ForeignKey(Movie, related_name="movie_screening", on_delete=models.CASCADE, null=True)
    screen = models.ForeignKey(Screen, related_name="screen", on_delete=models.CASCADE, null=True)
    festival = models.ForeignKey(Festival, related_name="festival", on_delete=models.CASCADE, null=True)        
    tag = models.ManyToManyField(Tag, related_name="screening_tag", blank=True)
    #objects = models.Manager()
    #objects_by_day = ScreeningManager()
    
    def __str__(self):
        return self.screening_datetime.strftime('%d/%m/%Y %H:%M')+' ('+self.screen.room_name +') : ' + self.movie.title


