from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User',  on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    tags = models.ManyToManyField('blog.Tag', related_name='tags', blank=True, null=True)
    images = models.ManyToManyField('blog.Image_Post', related_name='images', blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def __str__(self):
        return self.title
    
    def approved_comments(self):
        return self.comments.filter(approved_comment=True)
    
    def tag_list(self):
        return self.tags

class Comment(models.Model):
    post = models.ForeignKey('blog.Post',  on_delete=models.CASCADE,  related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    
    def approve(self):
        self.approved_comment = True
        self.save()
        
    def __str__(self):
        return self.text

class Tag(models.Model):
    #post = models.ManyToManyField('blog.Post',  related_name='tags')
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Image_Post(models.Model):    
    image_file = models.ImageField(upload_to = 'img_post/', default='img_post/no-img.jpg')