from django.shortcuts import render, get_object_or_404
from .models import Movie, Festival, Screen, Screening
import datetime

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
def movie_list(request):
    movies = Movie.objects.all
    url_img="https://image.tmdb.org/t/p/w92"
    return render(request,  'bifffidus/movie_list.html',  {'movies': movies, 'url_img' : url_img,})

def movie_detail(request, pk):
    movie = get_object_or_404(Movie,  pk=pk)
    url_img="https://image.tmdb.org/t/p/w185"
    return render(request,  'bifffidus/movie_detail.html',  {'movie': movie, 'url_img' : url_img,})

def movie_by_festival(request, pk):
    sql = '''   SELECT * 
                FROM bifffidus_movie,bifffidus_screening 
                WHERE bifffidus_movie.id = bifffidus_screening.movie_id 
                    AND bifffidus_screening.festival_id = %u
                GROUP BY bifffidus_movie.id 
                ORDER BY bifffidus_movie.title   
                    ''' % (pk)
    movies = Screening.objects.raw(sql)  

    dates = get_dates_by_festival(pk)
    return render(request, 'bifffidus/movie_by_festival.html', {'movies':movies, 'dates':dates})

def festival_list(request):
    festivals = Festival.objects.all
    return render(request, 'bifffidus/festival_list.html', {'festivals': festivals})

def festival_detail(request, pk):
    festival = get_object_or_404(Festival, pk=pk)    
    screenings = Screening.objects.filter(festival_id=pk).order_by('screening_datetime')
    return render(request, 'bifffidus/festival_detail.html', {'festival': festival, 'screenings':screenings})

def movie_by_date(request,year,  month,  day):      
    screenings = Screening.objects.filter(screening_datetime__date=datetime.date(year, month, day))
    return render(request, 'bifffidus/movie_by_date.html', {'screenings': screenings})
   