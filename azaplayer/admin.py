from django.contrib import admin
from .models import Audio_Post
# Register your models here.

@admin.register(Audio_Post)
class Audio_PostAdmin(admin.ModelAdmin):
    list_display = ('title','audiofile')