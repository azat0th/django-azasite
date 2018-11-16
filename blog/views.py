from django.shortcuts import render,  get_object_or_404,  redirect
from .models import Post,  Comment
from django.utils import timezone
from .forms import PostForm,  CommentForm
from django.contrib.auth.decorators import login_required
import datetime

#for sidebar purpose, this function regroup all dates where posts have been published and couple it with the number of posts of that date
#it is use to show a list on a sidebar of the website on any view
def get_post_by_date_list():
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #initialising var post_date_list which return tuple (datetime.date(y, m, d), int) 
    post_date_list=[]
    #navigating the posts to access to their tags objects assuming 1 post has a unique date
    #so we can break if the date is already in the list and increase the post-counter
    for post in posts:
        flag = 0
        for i, v in enumerate(post_date_list):
            #if the date is in post_date_list, we increase the counter by 1
            if v[0]== post.published_date.date():
                post_date_list[i] = (post_date_list[i][0],  post_date_list[i][1]+1)
                flag = 1
                break
        #if the post date is not in the list, we increase by 1 the post counter
        if flag == 0:
            post_date_list.append((post.published_date.date(), 1))    
    return post_date_list
    
#for sidebar purpose, this function regroup all tags and count posts by tag
#it is use to show a list on a sidebar of the website on any view
def get_post_by_tag_list():
    posts = Post.objects.filter(published_date__lte=timezone.now())
    post_tag_list=[]    
    for post in posts:       
        for tag in post.tags.all():
            flag=0
            for i, v in enumerate(post_tag_list):
                if(v[1]==tag):
                    post_tag_list[i] = (post_tag_list[i][0], post_tag_list[i][1],  post_tag_list[i][2]+1)
                    flag = 1
                    break
            if flag == 0:
                post_tag_list.append((tag.pk , tag, 1))
    return post_tag_list

# VIEWS   

# View post_list: show all posts 
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    dates = get_post_by_date_list()
    tags = get_post_by_tag_list()   
    return render(request,  'blog/post_list.html',  {'posts': posts,  'sidebar': 1,  'tags':tags,  'dates':dates})

# View post list of a day
def post_list_by_day(request, year,  month,  day):
    posts = Post.objects.filter(published_date__date=datetime.date(year, month, day)).order_by('published_date')
    dates = get_post_by_date_list()
    tags =get_post_by_tag_list()
    return render(request,  'blog/post_list.html',  {'posts': posts,  'sidebar': 1,  'tags':tags,  'dates':dates})

# View post list of a tag
def post_list_by_tag(request,  pk):
    posts = Post.objects.filter(tags=pk)
    dates = get_post_by_date_list()
    tags =get_post_by_tag_list()
    return render(request,  'blog/post_list.html',  {'posts':posts,  'sidebar':1,  'tags':tags,  'dates':dates})

#View unique post
def post_detail(request, pk):
    post = get_object_or_404(Post,  pk=pk)
    dates = get_post_by_date_list()
    tags =get_post_by_tag_list()
    return render(request,  'blog/post_detail.html',  {'post': post,  'sidebar':1,  'tags':tags,   'dates':dates})

@login_required
# Add a post as logged member
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request,  'blog/post_edit.html',  {'form': form})

@login_required    
# Edit a post as logged member
def post_edit(request,  pk):
    post = get_object_or_404(Post,  pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST,  instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail',  pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request,  'blog/post_edit.html',  {'form': form})
    
@login_required
#List of posts to be published as logged member
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html',  {'posts': posts})

@login_required
def post_publish(request,  pk):
    post = get_object_or_404(Post,  pk=pk)
    post.publish()
    return redirect('post_detail',  pk=pk)
    
@login_required
def post_remove(request,  pk):
    post = get_object_or_404(Post,  pk=pk)
    post.delete()
    return redirect('post_list')

def add_comment_to_post(request,  pk):
    post = get_object_or_404(Post,  pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
            form = CommentForm()
    
    return render(request,  'blog/add_comment_to_post.html',  {'form': form})

@login_required    
def comment_remove(request, pk):
    comment = get_object_or_404(Comment,  pk=pk)
    comment.delete()
    return redirect('post_detail',  pk=comment.post.pk)

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment,  pk=pk)
    comment.approve()
    return redirect('post_detail',  pk=comment.post.pk)
