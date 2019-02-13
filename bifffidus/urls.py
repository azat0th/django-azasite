from django.urls import path
from . import views

urlpatterns = [
    path('bifffidus/', views.main_page,  name='main_page'),
    path('bifffidus/movie/<int:pk>/',  views.movie_detail,  name='movie_detail'),

    path('bifffidus/festival/', views.festival_list,  name='festival_list'),
    path('bifffidus/festival/<int:pk>/', views.festival_detail,  name='festival_detail'),

    path('bifffidus/movielist/<int:year>/<int:month>/<int:day>/', views.movie_by_date, name='movie_by_date'),
    path('bifffidus/movielist/<int:pk>/', views.movie_by_festival, name='movie_by_festival'),
    
    path('bifffidus/person/', views.person_list, name='person_list'),
    path('bifffidus/person/<int:pk>', views.person_detail, name='person_detail'),
    
    path('bifffidus/genre/', views.genre_list, name='genre_list'),
    path('bifffidus/genre/<int:pk>', views.genre_detail, name='genre_detail'),
    
    path('bifffidus/country/', views.country_list, name='country_list'),
    path('bifffidus/country/<int:pk>', views.country_detail, name='country_detail'),
    
    path('bifffidus/tag/', views.tag_list, name='tag_list'),
    path('bifffidus/tag/<int:pk>', views.tag_detail, name='tag_detail'),
    
    
]
