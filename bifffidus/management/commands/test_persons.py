'''
Created on 19 nov. 2018

@author: aza

'''

from xml.dom import minidom
from django.core.management.base import BaseCommand, CommandError
import datetime
from bifffidus.models import Festival, Movie, Screen, Screening, Place , Tag, Job
from bifffidus.models import Genre, Spoken_Language, Production_Company 
from bifffidus.models import Person, Country, Cast, Crew, Tag_Type, Department
from django.utils import timezone
from django.shortcuts import get_object_or_404


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
class Command(BaseCommand):
    help = 'Testing persons in db'

    def handle(self, *args, **options):
        '''persons = Person.objects.all()      
        n = 0  
        for p in persons:
            movie_list = Movie.objects.filter(crew__person_id=p.pk)
            movies = []
            for movie in movie_list:
                if(movie not in movies):
                    movies.append(movie)
            if len(movies) > 1 :
                n += 1
                print("{person}: {nmov}".format(person=p, nmov=len(movies)))
                #crews = Crew.objects.filter(person__id=p.pk)
                for m in movies:
                    print("{movie}:{jobs}".format(movie=m,jobs=m.get_person_crew_str(p.id)))       
        
        print("nombre de personnes : {nbpersons}".format(nbpersons=n))
     '''
        jobs = Job.objects.filter(department__name="crew")
        for j in jobs:
            print(j)
        
        print("n jobs = {nj}".format(nj=len(jobs)) )