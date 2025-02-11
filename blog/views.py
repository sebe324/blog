from django.shortcuts import render

from django.shortcuts import render
from blog.models import Post, Comment, Category, Project, Technology
import logging
from django.http import HttpResponseRedirect
from blog.forms import CommentForm
import random

logger = logging.getLogger('django')
def get_last_n(lst, n):
    yield lst[len(lst)-n:len(lst)]
def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")[:2]
    previews = []
    dates = []
    for post in posts:
        previews.append(post.body[:200])
        dates.append(post.created_on.date)    
    amount_of_projects = len(Project.objects.all())
    random_projs = random.sample(range(amount_of_projects), 3 if amount_of_projects>=3 else amount_of_projects)
    projects=[]
    for i in random_projs:
        projects.append(Project.objects.all()[random_projs[i]])
    technologies=[]
    for project in projects:
        technologies.append(Technology.objects.all().filter(projects=project))
    project_cards = zip(projects,technologies)
    context = {
        "post_cards": zip(posts,previews,dates),
        "project_cards":project_cards
    }
    return render(request, "blog/index.html",context)


def blog_category(request, category):
    posts =  Post.objects.filter(categories__name__contains=category).order_by('-created_on')
    previews = []
    dates = []
    for post in posts:
        previews.append(post.body[:200])
        dates.append(post.created_on.date)

    context = {
        "category":category,
        "elements": zip(posts,previews,dates),
    }
    return render(request,"blog/category.html",context)

def blog_post(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author = form.cleaned_data["author"],
                body = form.cleaned_data["body"],
                post=post
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)
        
    context = {
        "post":post,
        "comments":comments,
        "form": form
    }
    return render(request,"blog/post.html",context)
    
def blog_allprojects(request):
    projects = Project.objects.all()
    technologies=[]
    for project in projects:
        technologies.append(Technology.objects.all().filter(projects=project))
    project_cards = zip(projects,technologies)
    context = {
        "project_cards":project_cards
    }
    return render(request,"blog/allprojects.html",context)

def blog_allposts(request):
    posts = Post.objects.all().order_by("-created_on")
    previews = []
    dates = []
    for post in posts:
        previews.append(post.body[:200])
        dates.append(post.created_on.date)
    context = {
        "post_cards": zip(posts,previews,dates),
    }
    return render(request,"blog/allposts.html",context)