from django.urls import path
from . import views

urlpatterns = [
    path('bifffidus/', views.movie_list,  name='movie_list'),
    path('bifffidus/festival/', views.festival_list,  name='festival_list'),
    path('bifffidus/movie/<int:pk>/',  views.movie_detail,  name='movie_detail'),
    path('bifffidus/festival/<int:pk>/', views.festival_detail,  name='festival_detail'),
    path('bifffidus/movielist/<int:year>/<int:month>/<int:day>/', views.movie_by_date, name='movie_by_date'),
    path('bifffidus/movielist/<int:pk>/', views.movie_by_festival, name='movie_by_festival'),
]
