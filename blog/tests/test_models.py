from django.test import TestCase
from blog.models import Post, Comment, Tag, Image_Post
from builtins import classmethod
from datetime import datetime, timedelta
# Create your tests here.
class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Post.objects.create(title='Test Title', text='bla bla bla', author_id='1')
    
    def test_title_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')
    
    def test_title_max_length(self):
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field('title').max_length
        self.assertEquals(max_length, 200)
        
    def test_author_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('author').verbose_name
        self.assertEquals(field_label, 'author')

    def test_text_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('text').verbose_name
        self.assertEquals(field_label, 'text')
        
    def test_created_date_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('created_date').verbose_name
        self.assertEquals(field_label, 'created date')
        
    def test_published_date_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('published_date').verbose_name
        self.assertEquals(field_label, 'published date')
        
    def test_tags_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('tags').verbose_name
        self.assertEquals(field_label, 'tags')
        
    def test_images_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('images').verbose_name
        self.assertEquals(field_label, 'images')
    
    def test_is_recent_with_future_post(self):
        futur_post = Post(published_date=datetime.now() + timedelta(days=20))
        self.assertEqual(futur_post.is_recent(),False)
        

class CommentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Comment.objects.create(text='Test Text comment bla bla bla', post_id='1')
        
    def test_post_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('post').verbose_name
        self.assertEquals(field_label, 'post')
        
    def test_author_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('author').verbose_name
        self.assertEquals(field_label, 'author')
    
    def test_author_max_length(self):
        comment = Comment.objects.get(id=1)
        max_length = comment._meta.get_field('author').max_length
        self.assertEquals(max_length, 150)
        
    def test_text_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('text').verbose_name
        self.assertEquals(field_label, 'text')
        
    def test_created_date_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('created_date').verbose_name
        self.assertEquals(field_label, 'created date')
     
    def test_approved_comment_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('approved_comment').verbose_name
        self.assertEquals(field_label, 'approved comment')
        
class TagModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Tag.objects.create(name='Test Tag')
        
    def test_name_label(self):
        tag = Tag.objects.get(id=1)
        field_label = tag._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')
    
    def test_name_max_length(self):
        tag = Tag.objects.get(id=1)
        max_length = tag._meta.get_field('name').max_length
        self.assertEquals(max_length, 150)

class Image_PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Image_Post.objects.create()
        
    def test_image_file_label(self):
        image_post = Image_Post.objects.get(id=1)
        field_label = image_post._meta.get_field('image_file').verbose_name
        self.assertEquals(field_label, 'image file')
                