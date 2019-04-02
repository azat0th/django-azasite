from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page,  name='main_page'),
    path('bifffidus/', views.main_page, name='main_page'),
    path('movie/<int:pk>/',  views.movie_detail,  name='movie_detail'),

    path('festival/', views.festival_list,  name='festival_list'),
    path('festival/<int:pk>/', views.festival_detail,  name='festival_detail'),

    path('movielist/<int:year>/<int:month>/<int:day>/', views.movie_by_date, name='movie_by_date'),
    path('movielist/<int:pk>/', views.movie_by_festival, name='movie_by_festival'),
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
