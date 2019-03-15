'''
Created on 19 nov. 2018

@author: aza

xml structure skeleton for entry file :

<?xml version="1.0" encoding="UTF-8"?>
<festival title="Festival Title" start_date="day/month/year" end_date="day/month/year">
    <place name="Place 1">
        <screen>room_name</screen>        
    </place>
    <place name="Place 2">
        <screen>room_name</screen>
    </place>    
    <movie>
        <title>movie title</title>
        <imdb_link>imdb link: like tt0808096</imdb_link>
        <screenings>
            <screening screen="room_name">day/month/year hour:minutes</screening>                            
        </screenings>
        <tag>tag_name</tag>
    </movie>
    <movie>
    ...
    </movie>
</festival>

note: 
    day/month/year hour:minutes 
    example : 28/12/2018 20:30
    
    imdb_link : not entire url, just id number like tt*******  
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
    help = 'Populate the db with a xml'

    def add_arguments(self, parser):
        parser.add_argument('import_file', nargs='+')

    def handle(self, *args, **options):
        #initiate DB with default vals :
        type_list=["competitions","awards","others"]
        for typetag in type_list:
            tag_in_db = Tag_Type.objects.filter(name__exact=typetag)
            if tag_in_db:
                print("tag_type déjà en db:{tag}".format(tag=typetag))
            else:
                print("tag_type à ajouter")
                tag_type = Tag_Type()
                tag_type.name = typetag
                tag_type.save()
        tag_list = ["grand prix","silver","melies","audience","thriller award", "critics award","7th orbit award"]
        
        for tagname in tag_list:
            tag_in_db = Tag.objects.filter(name__exact=tagname)
            if tag_in_db:
                print("tag déjà en db:{tag}".format(tag=tagname))
            else:
                tag_type = get_object_or_404(Tag_Type, name="awards")
                tag = Tag()
                tag.name = tagname
                tag.tag_type = tag_type
                tag.save()
            
        tag_list = ["european competition","international competition","thriller competition","7th orbit"]
        for tagname in tag_list:
            tag_in_db = Tag.objects.filter(name__exact=tagname)
            if tag_in_db:
                print("tag déjà en db:{tag}".format(tag=tagname))
            else:
                tag_type = get_object_or_404(Tag_Type, name="competitions")
                tag = Tag()
                tag.name = tagname
                tag.tag_type = tag_type
                tag.save()
        
        tag_list = ["7th orbit special mention","thriller special mention"]
        for tagname in tag_list:
            tag_in_db = Tag.objects.filter(name__exact=tagname)
            if tag_in_db:
                print("tag déjà en db:{tag}".format(tag=tagname))
            else:
                tag_type = get_object_or_404(Tag_Type, name="awards")
                tag = Tag()
                tag.name = tagname
                tag.tag_type = tag_type
                tag.hidden = True
                tag.save()            
            
                    
        for file in options['import_file']:
            DOMTree = minidom.parse(file)
            collection = DOMTree.documentElement
            festival = Festival() 
            if collection.hasAttribute("title"):
                print("Root element : %s" % collection.getAttribute("title"))
                festival.title = collection.getAttribute("title")
                if collection.hasAttribute("start_date"):
                    print("Root element : start_date = %s" % collection.getAttribute("start_date"))
                    format_str = '%d/%m/%Y' # The date format
                    festival.start_date = datetime.datetime.strptime(collection.getAttribute("start_date"), format_str)
                                   
                if collection.hasAttribute("end_date"):
                    print("Root element : end_date = %s" % collection.getAttribute("end_date"))                    
                    format_str = '%d/%m/%Y' # The date format
                    festival.end_date = datetime.datetime.strptime(collection.getAttribute("end_date"), format_str)
                
                if collection.hasAttribute("poster_path"):
                    print("Root element : poster_path = %s" % collection.getAttribute("poster_path"))
                    festival.poster_path = collection.getAttribute("poster_path")                
                
            if(len(festival.title)>0):
                festival.save()
                print()
            else:
                assert('Aborted,No Festival title, impossible to link the movies.')
                
            places = collection.getElementsByTagName("place")
            print("Nombre de lieux: "+str(len(places)))
            for place in places:
                print(bcolors.HEADER+"***place***"+bcolors.ENDC)
                place_name = place.getAttribute("name")
                print("placename= {place_name}".format(place_name=place_name))
                place_in_db = Place.objects.filter(name__exact=place_name)
                print(place_in_db)
                p = Place()
                if(len(place_name)>0):
                    if(len(place_in_db)==1):#déjà en db
                        print(bcolors.OKGREEN+"[Place] already in DB : {place}".format(place=place_name)+bcolors.ENDC)
                        p = Place.objects.get(name=place_name)
                    elif(len(place_in_db)==0):#pas encore en db
                        p.name = place_name
                        print(bcolors.WARNING+"[Place] to add : {place}".format(place=place_name)+bcolors.WARNING)
                        p.save()
                        screens = place.getElementsByTagName("screen")
                        for screen in screens:
                            screen_name = screen.firstChild.data
                            if(len(screen_name)>0):                            
                                s = Screen()
                                s.room_name = screen_name
                                s.save()
                                p.screen.add(s)                                            
                        
                    else:
                        print(bcolors.FAIL+'A place with the same name is already in DB'+bcolors.ENDC)
                        
                    p.save()
                    festival.place.add(p)
                    
                else:
                    print(bcolors.FAIL+'The place is blank'+bcolors.ENDC)
                    pass 
            festival.save()
            # Get all the movies in the collection
            movies = collection.getElementsByTagName("movie")
            print("Nombre de films: "+str(len(movies)))
            movies_added = 0
            for movie in movies:
                print(bcolors.HEADER+"***movie***"+bcolors.ENDC)
                m = Movie()
                
                title = movie.getAttribute("title")
                imdb_id = movie.getAttribute("imdb_id")
                                                
                if(len(title)>=0):
                    print(bcolors.OKGREEN+"{title} [imdb:{imdb_id}]".format(title=title, imdb_id=imdb_id, tmdb_id=m.tmdb_id)+bcolors.ENDC)                    
                    if(Movie.objects.filter(title__exact=title)):
                        print(bcolors.FAIL+'A Movie with the same title is already in DB'+bcolors.ENDC)
                    if(len(imdb_id)>0 and Movie.objects.filter(imdb_id__exact=imdb_id)):
                        print(bcolors.FAIL+'A Movie with the same imdb_id is already in DB'+bcolors.ENDC)
                        m = get_object_or_404(Movie,imdb_id=imdb_id)
                    else:                        
                        m.title = ""+title
                        m.imdb_id = ""+imdb_id                        
                        if(movie.getElementsByTagName("tmdb")):
                            
                            tmdb = movie.getElementsByTagName("tmdb")[0]
                            #m.tmdb_id = tmdb.getAttribute("id")
                            tmdb_id = ''
                            if(tmdb.hasAttribute("id")):
                                tmdb_id = tmdb.getAttribute("id")
                            
                            print(bcolors.OKGREEN+"[tmdb:{tmdb_id}]".format(title=m.title, imdb_id=m.imdb_id, tmdb_id=m.tmdb_id)+bcolors.ENDC)
                            
                            backdrop_path = ''
                            if(tmdb.getElementsByTagName('backdrop_path')[0].hasChildNodes()):
                                backdrop_path = tmdb.getElementsByTagName('backdrop_path')[0].childNodes[0].data
                                #m.backdrop_path = backdrop_path
                            
                            original_language = ''
                            if(tmdb.getElementsByTagName('original_language')[0].hasChildNodes()):
                                original_language = tmdb.getElementsByTagName('original_language')[0].childNodes[0].data
                                #m.original_language = original_language
                            
                            overview = ''
                            if(tmdb.getElementsByTagName('overview')[0].hasChildNodes()):
                                overview = tmdb.getElementsByTagName('overview')[0].childNodes[0].data
                                #m.overview = overview
                            
                            original_title = ''
                            if(tmdb.getElementsByTagName('original_title')[0].hasChildNodes()):
                                original_title = tmdb.getElementsByTagName('original_title')[0].childNodes[0].data
                                #m.original_title = original_title
                            
                            poster_path = ''
                            if(tmdb.getElementsByTagName('poster_path')[0].hasChildNodes()):
                                poster_path = tmdb.getElementsByTagName('poster_path')[0].childNodes[0].data
                                #m.poster_path = poster_path
                            
                            
                            if(tmdb.getElementsByTagName('release_date')[0].hasChildNodes()):
                                release_date_str = tmdb.getElementsByTagName('release_date')[0].childNodes[0].data
                                release_date = 0
                                if(len(release_date_str)>8):
                                    release_date = datetime.datetime.strptime(release_date_str, '%Y-%m-%d')
                                #m.release_date = release_date
                            
                            runtime = 0
                            if(tmdb.getElementsByTagName('runtime')[0].hasChildNodes()):
                                runtime = tmdb.getElementsByTagName('runtime')[0].childNodes[0].data
                                if(runtime=="None"):
                                    runtime = 0
                                #m.runtime = runtime
                            
                            tagline = ''
                            if(tmdb.getElementsByTagName('tagline')[0].hasChildNodes()):
                                tagline = tmdb.getElementsByTagName('tagline')[0].childNodes[0].data
                                #m.tagline = tagline
                            
                            m = Movie.objects.create_movie(title, imdb_id, tmdb_id, overview, runtime, tagline, backdrop_path, poster_path, original_language, original_title, release_date)
                            
                            m.save()   
                            genres_Node = tmdb.getElementsByTagName("genre")
                            print("[Genre] Found : {nb}".format(nb=len(genres_Node)))
                            for genre_N in genres_Node:
                                genre = genre_N.childNodes[0].data
                                genre_in_db = Genre.objects.filter(name__exact=genre) 
                                if(len(genre_in_db)==1):
                                    print(bcolors.OKGREEN+"[Genre] already in DB : {genre}".format(genre=genre)+bcolors.ENDC)
                                    g = Genre.objects.get(name=genre)
                                    m.genre.add(g)
                                elif(len(genre_in_db)==0):
                                    print(bcolors.WARNING+"[Genre] to add : {genre}".format(genre=genre)+bcolors.ENDC)
                                    g = Genre()
                                    g.name = genre
                                    g.save()
                                    m.genre.add(g)                                                                
                                else:
                                    print(bcolors.FAIL+"[Genre] Erreur lors de la correspondance des genres avec la DB:") 
                                    print("[Genre] Nombre de Genres trouvés en db = {nb}".format(nb=len(genre_in_db))+bcolors.ENDC)                        
                                
                            companies_Node = tmdb.getElementsByTagName("production_company")
                            print("[Production_Company] found : {nb}".format(nb=len(companies_Node)))                    
                            for company_N in companies_Node:
                                company = company_N.childNodes[0].data
                                company_in_db = Production_Company.objects.filter(name__exact=company)
                                if(len(company_in_db)==1):
                                    print(bcolors.OKGREEN+"[Production_Company] already in DB : {company}".format(company=company)+bcolors.ENDC)
                                    p = Production_Company.objects.get(name=company)
                                    m.production_company.add(p)
                                elif(len(company_in_db)==0):
                                    print(bcolors.WARNING+"[Production_Company] to add : {company}".format(company=company)+bcolors.ENDC)
                                    p = Production_Company()
                                    p.name = company
                                    p.save()
                                    m.production_company.add(p)
                                else:
                                    print(bcolors.FAIL+"[Production_Company] Erreur lors de la correspondance des production_company avec la DB:")
                                    print("[Production_Company] Nombre de Production_Company trouvés en db= {nb}".format(nb=len(company_in_db))+bcolors.ENDC)
                                                           
                            countries_Node = tmdb.getElementsByTagName("country")
                            print("[Country] found: {nb}".format(nb=len(countries_Node)))
                            for country_N in countries_Node:
                                country = country_N.childNodes[0].data
                                country_in_db = Country.objects.filter(name__exact=country)
                                if(len(country_in_db)==1):
                                    print(bcolors.OKGREEN+"[Country] already in DB : {country}".format(country=country)+bcolors.ENDC)
                                    c = Country.objects.get(name=country)
                                    m.country.add(c)
                                elif(len(country_in_db)==0):
                                    print(bcolors.WARNING+"[Country] to add : {country}".format(country=country)+bcolors.ENDC)
                                    c = Country()
                                    c.name = country
                                    c.save()
                                    m.country.add(c)
                                else:
                                    print(bcolors.FAIL+"[Country] Erreur lors de la correspondance des country avec la DB:")
                                    print("[Country] Nombre de country trouvés en db= {nb}".format(nb=len(country_in_db))+bcolors.ENDC)                            
                                                    
                            spoken_language_Node = tmdb.getElementsByTagName("spoken_languages")
                            print("[Spoken_Language] found : {nb}".format(nb=len(spoken_language_Node)))
                            for lang_N in spoken_language_Node:
                                if(lang_N.childNodes.length>0):
                                    lang = lang_N.childNodes[0].data
                                    lang_in_db = Spoken_Language.objects.filter(name__exact=lang)
                                    if(len(lang_in_db)==1):
                                        print(bcolors.OKGREEN+"[Spoken_Language] already in DB : {lang}".format(lang=lang)+bcolors.ENDC)
                                        l = Spoken_Language.objects.get(name=lang)
                                        m.spoken_language.add(l)
                                    elif(len(lang_in_db)==0):
                                        print(bcolors.WARNING+"[Spoken_Language] to add : {lang}".format(lang=lang)+bcolors.ENDC)
                                        l = Spoken_Language()
                                        l.name = lang
                                        l.save()
                                        m.spoken_language.add(l)
                                    else:
                                        print(bcolors.FAIL+"[Spoken_Language] Erreur lors de la correspondance des Spoken_Language avec la DB:")
                                        print("[Spoken_Language] Nombre de Spoken_Language trouvés en db= {nb}".format(nb=len(lang_in_db))+bcolors.ENDC)

                                                        
                            actor_Node = tmdb.getElementsByTagName("actor")
                            nbactor = len(actor_Node)
                            print("nb actor : {nb}".format(nb=nbactor))
                            count_nbactor = 0
                            for actor in actor_Node:                                
                                character = actor.getAttribute("character")
                                tmdb_id = actor.getAttribute("tmdb_id")
                                name = actor.childNodes[0].data                            
                                #print("[Actor] %s as %s" % (name, character))
                                #check if actor is in db
                                p = Person()
                                person_in_db = Person.objects.filter(tmdb_id=tmdb_id)
                                
                                count_nbactor = count_nbactor + 1
                                if(len(person_in_db)==1):
                                    print(bcolors.OKGREEN+"[Person] already in DB [{count_nbactor}/{nbactor}]: {name}                       ".format(name=name, count_nbactor=count_nbactor, nbactor=nbactor)+bcolors.ENDC, end='\r')
                                    p = Person.objects.get(tmdb_id=tmdb_id)
                                    
                                elif(len(person_in_db)==0):
                                    print(bcolors.WARNING+"[Person] to add [{count_nbactor}/{nbactor}]: {name}                       ".format(name=name, count_nbactor=count_nbactor, nbactor=nbactor)+bcolors.ENDC, end='\r')
                                    p.name = name
                                    p.tmdb_id = tmdb_id
                                    p.profile_path = actor.getAttribute("profile_path")
                                    p.gender = actor.getAttribute("gender")
                                    p.save()                                    
                                else:
                                    print(bcolors.FAIL+"[Person] Erreur lors de la correspondance avec la DB:")
                                    print("[Person] Nombre de Persons trouvés en db= {nb}".format(nb=len(person_in_db))+bcolors.ENDC)

                                c = Cast()
                                c.character = character
                                c.order = actor.getAttribute("order")
                                c.person = p
                                #c.movie = m
                                c.save()
                                m.cast.add(c)
                                m.save()                    
                                
                                
                            print('', end='\n')
                            crew_Node = tmdb.getElementsByTagName("crew")
                            nbcrew = len(crew_Node)
                            print("nb crew : {nb}".format(nb=nbcrew))
                            count_nbcrew = 0
                            for crew in crew_Node:                                
                                jobname = crew.getAttribute("job")
                                department = crew.getAttribute("department")
                                
                                department_in_db = Department.objects.filter(name=department)
                                d = Department()
                                if(len(department_in_db)==1):
                                    d = department_in_db[0]
                                elif(len(department_in_db)==0):
                                    d.name = department
                                    d.save() 
                                else:
                                    print(bcolors.FAIL+"[Department] Erreur lors de la correspondance avec la DB"+bcolors.ENDC)
                                
                                job_in_db = Job.objects.filter(jobname=jobname)
                                j = Job()
                                if(len(job_in_db)==1):
                                    j = job_in_db[0]
                                elif(len(job_in_db)==0):
                                    j.jobname = jobname
                                    j.department = d
                                    j.save() 
                                else:
                                    print(bcolors.FAIL+"[Job] Erreur lors de la correspondance avec la DB"+bcolors.ENDC)
                                tmdb_id = crew.getAttribute("tmdb_id")
                                name = crew.childNodes[0].data
                                count_nbcrew = count_nbcrew + 1
                                
                                p = Person()
                                person_in_db = Person.objects.filter(tmdb_id=tmdb_id)
                                
                                if(len(person_in_db)==1):
                                    print(bcolors.OKGREEN+"[Person] already in DB [{count_nbcrew}/{nbcrew}]: {name}                       ".format(name=name, count_nbcrew=count_nbcrew, nbcrew=nbcrew)+bcolors.ENDC, end='\r')                                    
                                    p = person_in_db[0]
                                    
                                elif(len(person_in_db)==0):
                                    print(bcolors.WARNING+"[Person] to add [{count_nbcrew}/{nbcrew}]: {name}                              ".format(name=name, count_nbcrew=count_nbcrew, nbcrew=nbcrew)+bcolors.ENDC, end='\r')                                    
                                    p.name = name
                                    p.tmdb_id = tmdb_id
                                    p.profile_path = crew.getAttribute("profile_path")
                                    p.gender = crew.getAttribute("gender")
                                    p.save()
                                    
                                else:
                                    print(bcolors.FAIL+"[Person] Erreur lors de la correspondance avec la DB:")
                                    print("[Person] Nombre de Persons trouvés en db= {nb}".format(nb=len(person_in_db))+bcolors.ENDC)

                                c = Crew()
                                
                                c.job = j
                                c.person = p
                                #c.movie = m
                                c.save()
                                m.crew.add(c)                    
                                m.save()                                
                                
                        else:
                            print(bcolors.FAIL+"[TMDB_ID]: Empty"+bcolors.ENDC)    
                            m = Movie.objects.create_movie(title, "", "", "", 0, "", "", "", "", "",0)
                        print('\n')

                    screenings = movie.getElementsByTagName("screening")
                    print("[Screenings] found: {nb}".format(nb=len(screenings)))
                    for screening_Node in screenings:
                        if(screening_Node.childNodes[0].data):
                            s = Screening()
                            s.movie = m
                            s.save()
                            screening_datetime = datetime.datetime.strptime(screening_Node.childNodes[0].data, '%d/%m/%Y %H:%M')
                            
                            
               
                            screen = screening_Node.getAttribute('screen')
                            #screen_in_db = Screen.objects.get(room=screen)
                            screen_in_db = Screen.objects.filter(room_name__exact=screen)
                            if(len(screen_in_db)==1):
                                #screen déjà en db
                                print(bcolors.OKGREEN+"[Screening:Screen] already in DB : {screen}".format(screen=screen)+bcolors.ENDC)
                                s_in_db = Screen.objects.get(room_name=screen)
                                s.screen = s_in_db
                            elif(len(screen_in_db)==0):                                    
                                #screen pas dans la db
                                print(bcolors.WARNING+"[Screening:Screen] to add : {screen}".format(screen=screen)+bcolors.ENDC)
                                sc = Screen()
                                sc.room_name = screen
                                sc.save()
                                s.screen = sc
                            else:                                    
                                print(bcolors.FAIL+"[Screening:Screen] Erreur lors de la correspondance des Screenings avec la DB:")
                                print("[Screening] Screening trouvés en db= {nb}".format(nb=len(screen_in_db))+bcolors.ENDC)
                            
                            tags = movie.getElementsByTagName("tag")
                            print("[Tags] found: {nb}".format(nb=len(tags)))
                            
                            for tag_Node in tags:
                                if(len(tag_Node.firstChild.data)>0):
                                    tagname = tag_Node.firstChild.data
                                    t = Tag()                                    
                                    tag_in_db = Tag.objects.filter(name__exact=tagname)
                                    if(len(tag_in_db)==1): #déjà en db
                                        print(bcolors.OKGREEN+"[Tag] already in DB : {tag}".format(tag=tagname)+bcolors.ENDC)
                                        t_in_db = Tag.objects.get(name=tagname)
                                        t = t_in_db
                                        s.tag.add(t)
                                    elif(len(tag_in_db)==0): #pas encore en db    
                                        print(bcolors.WARNING+"[Tag] to add : {tag}".format(tag=tagname)+bcolors.ENDC)
                                        tag_type=get_object_or_404(Tag_Type, name="others")                                                                    
                                        t.name = tagname
                                        t.tag_type = tag_type
                                        t.save()
                                        s.tag.add(t)
                                    else:
                                        print(bcolors.FAIL+"[Tag] Erreur lors de la correspondance des tags avec la DB:")
                                        print("[Tag] Nombre de tags trouvés en db= {nb}".format(nb=len(tag_in_db))+bcolors.ENDC)
                                    
                                    s.save()
                                
                            
                            s.festival = festival
                            s.screening_datetime = screening_datetime 
                            s.save()                                                  
                                                                                            
                    #m.festival.add(festival)    
                    m.save()
                    movies_added += 1                
                print("\033[93m***end movie***\033[0m")
            print(bcolors.WARNING+"Nombre de films ajoutés à la DB : {nb}".format(nb=movies_added)+bcolors.ENDC)
            