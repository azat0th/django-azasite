from django.shortcuts import render, get_object_or_404
from .models import Movie, Festival, Screen, Screening, Person, Cast, Crew, Tag, Country, Genre, Tag_Movie_Festival, Job
import datetime
from django.core.paginator import Paginator
from .forms import  MovieSearchForm

def get_dates_by_festival(pk):    
    screenings = Screening.objects.filter(festival_id=pk)
    datelist=[]
    for screening in screenings:
        flag=0
        for i, v in enumerate(datelist):
            if(v[0]==screening.screening_datetime.date()):
                datelist[i] = (datelist[i][0], datelist[i][1]+1)
                flag = 1
                break
        if flag == 0:
            datelist.append((screening.screening_datetime.date(),1))
    return datelist

# Create your views here.

def main_page(request):
    nb_movie = Movie.objects.all().count()
    nb_person = Person.objects.all().count()
    nb_festival = Festival.objects.all().count()
     
    return render(request, 'bifffidus/main_page.html',{'nb_movie':nb_movie, 'nb_person': nb_person, 'nb_festival': nb_festival })

def movie_list(request):
    form = MovieSearchForm()
    search =''
    movie_title=''
    if request.method == 'GET':
             
        if form.is_valid():
            form = MovieSearchForm(request.GET)
            movie_title = request.GET['movie_title']             
        else:
            movie_title = request.GET.get('movie_title')          

    if(movie_title is None):        
        movie_list = Movie.objects.order_by('title').all()        
    else:
        movie_list = Movie.objects.filter(title__icontains=movie_title).order_by('title').all()
        search="movie_title="+movie_title 
        
    paginator = Paginator(movie_list, 25) #show 25 movies
    nb_movies = len(movie_list)
    print("resultat: "+search)
    page = request.GET.get('page')
        
    if(page is None):
        page = 1    
    
    movies = paginator.page(page)
    director = get_object_or_404(Job,  jobname="Director")    
    url_img="https://image.tmdb.org/t/p/w92"
    return render(request,  'bifffidus/movie_list.html',  {'movies': movies,'nb_movies': nb_movies, 'url_img' : url_img, 'form': form, 'director':director, 'search':search})

def movie_detail(request, pk):
    movie = get_object_or_404(Movie,  pk=pk)
    url_img="https://image.tmdb.org/t/p/w185"
    screenings = Screening.objects.filter(movie_id=pk)
    tags = Tag_Movie_Festival.objects.filter(movie_id=pk)
    #casting = Cast.objects.filter(movie_id=pk)
    #crew = Crew.objects.filter(movie_id=pk)
    print(movie)    
    return render(request,  'bifffidus/movie_detail.html',  {'movie': movie, 'url_img' : url_img, 'screenings' : screenings, 'tags' : tags})

def movie_by_festival(request, pk):
    sql = '''   SELECT        
                        bifffidus_movie.id,
                        bifffidus_movie.title,
                        bifffidus_person.name 
                FROM bifffidus_person, bifffidus_movie, bifffidus_screening, 
                    bifffidus_crew, bifffidus_job  
                WHERE
                    bifffidus_movie.id = bifffidus_crew.movie_id AND 
                    bifffidus_crew.person_id=bifffidus_person.id AND 
                    bifffidus_job.id = bifffidus_crew.job_id AND 
                    bifffidus_movie.id = bifffidus_screening.movie_id AND 
                    bifffidus_job.jobname = "Director" AND 
                    bifffidus_screening.festival_id= %u 
                ORDER BY bifffidus_movie.title
                ''' % (pk)    
    movies = Screening.objects.raw(sql)
    print(movies)
    url_img="https://image.tmdb.org/t/p/w92"
    dates = get_dates_by_festival(pk)
    return render(request, 'bifffidus/movie_by_festival.html', {'movies':movies, 'dates':dates, 'url_img' : url_img,})

def festival_list(request):
    festivals = Festival.objects.order_by('start_date').all
    return render(request, 'bifffidus/festival_list.html', {'festivals': festivals})

def festival_detail(request, pk):
    festival = get_object_or_404(Festival, pk=pk)    
    screenings = Screening.objects.filter(festival_id=pk).order_by('screening_datetime')
    url_img="https://image.tmdb.org/t/p/w45"
    return render(request, 'bifffidus/festival_detail.html', {'festival': festival, 'screenings':screenings, 'url_img': url_img,})

def movie_by_date(request, year,  month,  day):      
    screenings = Screening.objects.filter(screening_datetime__date=datetime.date(year, month, day))
    return render(request, 'bifffidus/movie_by_date.html', {'screenings': screenings})

def person_list(request):
    person_list = Person.objects.order_by('name').all()
    
    paginator = Paginator(person_list, 25) #show 25 movies
    nb_persons = len(person_list)
    page = request.GET.get('page')
    if(page is None):
        page = 1    
    persons = paginator.page(page)
    
    return render(request, 'bifffidus/person_list.html', {'persons': persons, 'nb_persons': nb_persons})

def person_detail(request, pk):
    person = get_object_or_404(Person, pk=pk)
    
    sql_cast = '''select bifffidus_movie.id,bifffidus_movie.title, bifffidus_cast.character
            from bifffidus_person, bifffidus_movie, bifffidus_cast, bifffidus_movie_cast 
            where bifffidus_movie.id = bifffidus_movie_cast.movie_id and
             bifffidus_movie_cast.cast_id = bifffidus_cast.id and 
             bifffidus_cast.person_id=bifffidus_person.id and       
             bifffidus_person.id= %u ;
    ''' % (pk)
    movie_cast = Movie.objects.raw(sql_cast)
    sql_crew = '''select bifffidus_movie.id,title,jobname 
            from bifffidus_person, bifffidus_movie, bifffidus_crew, bifffidus_job, bifffidus_movie_crew  
            where bifffidus_movie.id = bifffidus_movie_crew.movie_id and
             bifffidus_movie_crew.crew_id = bifffidus_crew.id and 
             bifffidus_crew.person_id=bifffidus_person.id and 
             bifffidus_job.id = bifffidus_crew.job_id and      
             bifffidus_person.id= %u ;
    ''' % (pk)
    movie_crew = Movie.objects.raw(sql_crew)   
    return render(request, 'bifffidus/person_detail.html', {'person': person, 'movie_cast' : movie_cast, 'movie_crew' : movie_crew})

def tag_list(request):
    tags = Tag.objects.order_by('tag_type','name').all
    return render(request, 'bifffidus/tag_list.html', {'tags': tags })

def tag_detail(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    tfms = Tag_Movie_Festival.objects.filter(tag__id=pk)
    return render(request, 'bifffidus/tag_detail.html', {'tag':tag, 'tfms':tfms})

def country_list(request):
    countries = Country.objects.order_by('name').all
    return render(request, 'bifffidus/country_list.html', {'countries': countries})

def country_detail(request,pk):
    country = get_object_or_404(Country, pk=pk)
    movies = Movie.objects.filter(country__id=pk).order_by('title')
    return render(request, 'bifffidus/country_detail.html', {'country':country, 'movies': movies})

def genre_list(request):
    genres = Genre.objects.order_by('name').all
    return render(request, 'bifffidus/genre_list.html', {'genres': genres})

def genre_detail(request,pk):
    genre = get_object_or_404(Genre, pk=pk)
    movies = Movie.objects.filter(genre__id=pk).order_by('title')
    return render(request, 'bifffidus/genre_detail.html', {'genre':genre, 'movies': movies})
