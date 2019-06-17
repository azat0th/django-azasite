from django.shortcuts import render, redirect, get_object_or_404
from .models import Image_Post, Audio_Post
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import AudioPostForm
import logging

try:
    import mutagen
except ImportError:
    import mutagenx as mutagen # Py3

from mutagen import MutagenError

# Create your views here.
def playlist(request):
    audioposts = Audio_Post.objects.order_by('title')
    return render(request,  'azaplayer/playlist.html',  {'audioposts': audioposts,  'sidebar': 1, })

@login_required
def audio_new(request):
# Add a post as logged member
    logger = logging.getLogger(__name__)

    if request.method == "POST":
        message=""
        form = AudioPostForm(request.POST, request.FILES)
        try:
            metadata = mutagen.File(request.FILES['audiofile'], easy=True)
            #logger.info(metadata)
        except MutagenError:
            print("Loading failed")
        if form.is_valid() and metadata != None:
            form.save()
            return redirect('playlist')
        else :
            message= "ERROR azaplayer.views.audio_new: Unable to upload the file. Is it a correct sound file?"
            #print(message)
            logger.info (message)
            return redirect('audio_new')
    else:
        form = AudioPostForm()
    return render(request,  'azaplayer/audio_edit.html',  {'form': form})

@login_required
def audio_remove(request,  pk):
    post = get_object_or_404(Audio_Post,  pk=pk)
    post.delete()
    return redirect('playlist')

@login_required
def audio_edit(request,pk):
    audiopost = get_object_or_404(Audio_Post,  pk=pk)
    if request.method == "POST":
        form = AudioPostForm(request.POST, request.FILES, instance=audiopost)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('playlist')
    else:
        form = AudioPostForm(instance=post)
    return render(request,  'azaplayer/audio_edit.html',  {'form': form})

