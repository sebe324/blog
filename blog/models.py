from django.db import models

# Create your models here.

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")

    def __str__(self):

        return self.title

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author} on '{self.post}'"

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=3000)
    repo_link = models.URLField(max_length=300)
    image = models.URLField()
    technologies = models.ManyToManyField("Technology", related_name="projects")
    def __str__(self):
        return self.title
    

class Technology(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = "Technologies"
    def __str__(self):
        return self.name