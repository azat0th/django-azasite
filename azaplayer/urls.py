from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('azaplayer/', views.playlist,  name='playlist'),
    path('azaplayer/audio/new/',  views.audio_new,  name='audio_new'),
    path('azaplayer/audio/<int:pk>/edit', views.audio_edit, name='audio_edit'),
    path('azaplayer/audio/<pk>/remove',  views.audio_remove,  name='audio_remove'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)