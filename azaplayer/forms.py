from django import forms
from .models import Audio_Post

class AudioPostForm(forms.ModelForm):
    
    class Meta:
        model = Audio_Post
        fields = ('title',  'audiofile', )


