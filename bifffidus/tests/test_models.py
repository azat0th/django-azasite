from django.test import TestCase
from bifffidus.models import Festival, Movie, Screen, Screening, Place 
from bifffidus.models import Genre, Spoken_Language, Production_Company 
from bifffidus.models import Person, Job, Country
import datetime


#class CreditModelTest(TestCase):
#class MovieManagerModelTest(TestCase):

class PersonModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Person.objects.create(name='Guillermo del Torro')
    
    def test_name_label(self):
        person = Person.objects.get(id=1)
        field_label = person._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')
    
    def test_name_max_length(self):
        person = Person.objects.get(id=1)
        max_length = person._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)

class JobModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Job.objects.create(name='Réalisateur')
    
    def test_name_label(self):
        job = Job.objects.get(id=1)
        field_label = job._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')
    
    def test_name_max_length(self):
        job = Job.objects.get(id=1)
        max_length = job._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)

class GenreModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Genre.objects.create(name='Fantasy')
    
    def test_name_label(self):
        genre = Genre.objects.get(id=1)
        field_label = genre._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        genre = Genre.objects.get(id=1)
        max_length = genre._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)

class Production_CompanyModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Production_Company.objects.create(name='Bifff Company')
    
    def test_name_label(self):
        production_company = Production_Company.objects.get(id=1)
        field_label = production_company._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')
        
    def test_name_max_length(self):
        production_company = Production_Company.objects.get(id=1)
        max_length = production_company._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)

class CountryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Country.objects.create(name='Belgium')
    
    def test_name_label(self):
        country = Country.objects.get(id=1)
        field_label = country._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')
        
    def test_name_max_length(self):
        country = Country.objects.get(id=1)
        max_length = country._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)
        

class Spoken_LanguageModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Spoken_Language.objects.create(name='Belgium')
    
    def test_name_label(self):
        spoken_language = Spoken_Language.objects.get(id=1)
        field_label = spoken_language._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        spoken_language = Spoken_Language.objects.get(id=1)
        max_length = spoken_language._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)        

class MovieModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Movie.objects.create(title='Titre du film')
    
    def test_title_label(self):
        movie = Movie.objects.get(id=1)
        field_label = movie._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')
    
    def test_title_max_length(self):
        movie = Movie.objects.get(id=1)
        max_length = movie._meta.get_field('title').max_length
        self.assertEquals(max_length, 250)
        
    def test_imdb_id_label(self):
        movie = Movie.objects.get(id=1)
        field_label = movie._meta.get_field('imdb_id').verbose_name
        self.assertEquals(field_label, 'imdb id')        
    
    def test_imdb_id_length(self):
        movie = Movie.objects.get(id=1)
        max_length = movie._meta.get_field('imdb_id').max_length
        self.assertEquals(max_length, 200)
    
    def test_tmdb_id_label(self):
        movie = Movie.objects.get(id=1)
        field_label = movie._meta.get_field('tmdb_id').verbose_name
        self.assertEquals(field_label, 'tmdb id')
    
    def test_tmdb_id_length(self):
        movie = Movie.objects.get(id=1)
        max_length = movie._meta.get_field('tmdb_id').max_length
        self.assertEquals(max_length, 200)

    def test_overview_label(self):
        movie = Movie.objects.get(id=1)
        field_label = movie._meta.get_field('overview').verbose_name
        self.assertEquals(field_label, 'overview')
                            
    def test_release_date_label(self):
        movie = Movie.objects.get(id=1)
        field_label = movie._meta.get_field('release_date').verbose_name
        self.assertEquals(field_label, 'release date')
        
    def test_runtime_label(self):
        movie = Movie.objects.get(id=1)
        field_label = movie._meta.get_field('runtime').verbose_name
        self.assertEquals(field_label, 'runtime')
    
    def test_tagline_label(self):
        movie = Movie.objects.get(id=1)
        field_label = movie._meta.get_field('tagline').verbose_name
        self.assertEquals(field_label, 'tagline')

    def test_backdrop_path_label(self):
        movie = Movie.objects.get(id=1)
        field_label = movie._meta.get_field('backdrop_path').verbose_name
        self.assertEquals(field_label, 'backdrop path')

    def test_backdrop_path_length(self):
        movie = Movie.objects.get(id=1)
        max_length = movie._meta.get_field('backdrop_path').max_length
        self.assertEquals(max_length, 200)        
    
    def test_poster_path_label(self):
        movie = Movie.objects.get(id=1)
        field_label = movie._meta.get_field('poster_path').verbose_name
        self.assertEquals(field_label, 'poster path')
        
    def test_poster_path_length(self):
        movie = Movie.objects.get(id=1)
        max_length = movie._meta.get_field('poster_path').max_length
        self.assertEquals(max_length, 200)         

    def test_original_language_label(self):
        movie = Movie.objects.get(id=1)
        field_label = movie._meta.get_field('original_language').verbose_name
        self.assertEquals(field_label, 'original language')

    def test_original_language_length(self):
        movie = Movie.objects.get(id=1)
        max_length = movie._meta.get_field('original_language').max_length
        self.assertEquals(max_length, 200)  
    
    def test_original_title_label(self):
        movie = Movie.objects.get(id=1)
        field_label = movie._meta.get_field('original_title').verbose_name
        self.assertEquals(field_label, 'original title')
          
    def test_original_title_length(self):
        movie = Movie.objects.get(id=1)
        max_length = movie._meta.get_field('original_title').max_length
        self.assertEquals(max_length, 250)        
        
    def test_get_absolute_url(self):
        movie = Movie.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(movie.get_absolute_url(), '/bifffidus/movie/1/')

class PlaceModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Place.objects.create(name='Bozart')        
    
    def test_name_label(self):
        place = Place.objects.get(id=1)
        field_label = place._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_length(self):
        place = Place.objects.get(id=1)
        max_length = place._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)        

class ScreenModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Screen.objects.create(room_name='Salle 1')        
    
    def test_room_name_label(self):
        screen = Screen.objects.get(id=1)
        field_label = screen._meta.get_field('room_name').verbose_name
        self.assertEquals(field_label, 'room name')
        
    def test_room_name_length(self):
        screen = Screen.objects.get(id=1)
        max_length = screen._meta.get_field('room_name').max_length
        self.assertEquals(max_length, 200)
        
class FestivalModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Festival.objects.create(title='Salle 1')        
    
    def test_title_label(self):
        festival = Festival.objects.get(id=1)
        field_label = festival._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_title_length(self):
        festival = Festival.objects.get(id=1)
        max_length = festival._meta.get_field('title').max_length
        self.assertEquals(max_length, 200)        

    def test_start_date_label(self):
        festival = Festival.objects.get(id=1)
        field_label = festival._meta.get_field('start_date').verbose_name
        self.assertEquals(field_label, 'start date')

    def test_end_date_label(self):
        festival = Festival.objects.get(id=1)
        field_label = festival._meta.get_field('end_date').verbose_name
        self.assertEquals(field_label, 'end date')
        
    def test_get_absolute_url(self):
        festival = Festival.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(festival.get_absolute_url(), '/bifffidus/festival/1/')
        
class ScreeningModelTest(TestCase):    
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        #Screening.objects.create(screening_datetime=datetime(18,4,18,20,30))     
        Screening.objects.create(id=1)
    def test_screening_datetime_label(self):
        screening = Screening.objects.get(id=1)
        field_label = screening._meta.get_field('screening_datetime').verbose_name
        self.assertEquals(field_label, 'screening datetime')