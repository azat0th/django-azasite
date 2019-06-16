from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.

class Post(models.Model):
    class Meta:
        permissions = (("can_post_on_blog", "Create or Update the posts"),)
    author = models.ForeignKey('auth.User',  on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    tags = models.ManyToManyField('blog.Tag', related_name='tags', blank=True)
    images = models.ManyToManyField('blog.Image_Post', related_name='images', blank=True)
    
    def is_recent(self):
        """ Return True if the post has been published in the last 30 days """
        return (datetime.now() - self.published_date).days < 30 and self.published_date < datetime.now()
    
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
    author = models.CharField(max_length=150)
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
    name = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name

class Image_Post(models.Model):
    title = models.CharField(max_length=200, default="")
    updated_date = models.DateTimeField(default = timezone.now)    
    image_file = models.ImageField(upload_to = 'img_post/', default='img_post/no-img.jpg')

    