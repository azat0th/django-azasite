from django.shortcuts import render,  get_object_or_404,  redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
import datetime
from django.apps import apps


# View post_list: show all posts 
def IndexView(request):
    applis = apps.get_models()
         
    return render(request,  'azasite/index.html',  {'applis': applis,  })