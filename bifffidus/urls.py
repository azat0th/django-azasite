from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page,  name='main_page'),
    path('bifffidus/', views.main_page, name='main_page'),
    path('movie/<int:pk>/',  views.movie_detail,  name='movie_detail'),

    path('festival/', views.festival_list,  name='festival_list'),
    path('festival/<int:pk>/', views.festival_detail,  name='festival_detail'),

    path('festival/<int:year>/<int:month>/<int:day>/', views.screenings_by_date, name='screenings_by_date'),
    path('festival/<int:pk>/list/', views.movie_by_festival, name='movie_by_festival'),
    path('festival/<int:pk>/competitions/', views.movie_by_festival_competitions, name='movie_by_festival_competitions'),
    path('festival/<int:pk>/palmares/', views.festival_palmares, name='festival_palmares'),
    path('movie/', views.movie_list, name='movie_list'),    
    
    path('person/', views.person_list, name='person_list'),
    
    path('person/<int:pk>', views.person_detail, name='person_detail'),
    
    path('genre/', views.genre_list, name='genre_list'),
    path('genre/<int:pk>', views.genre_detail, name='genre_detail'),
    
    path('country/', views.country_list, name='country_list'),
    path('country/<int:pk>', views.country_detail, name='country_detail'),
    
    path('tag/', views.tag_list, name='tag_list'),
    path('tag/<int:pk>', views.tag_detail, name='tag_detail'),
    
        
    
]
