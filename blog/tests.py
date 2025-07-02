from django.test import TestCase
from django.test import Client
from django.urls import reverse 
from .models import Post,Category, Technology, Project

class BlogTestCase(TestCase):
    def testBlogPosts(self):
        client = Client()
        response = client.get(reverse('blog:posts'))
        self.assertEqual(response.status_code,200)

    def testSingleBlog(self):
        client = Client()
        cat = Category.objects.create(name="mycategory")

        blogpost = Post.objects.create(title="placeholder", body="lorem ipsum")
        blogpost.categories.add(cat)
        response = client.get(reverse('blog:post',kwargs={'pk':1}))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,blogpost.title)

class ProjectsTestCase(TestCase):
    def testOneProject(self):
        client = Client()
        technology = Technology.objects.create(name='Python', color='.skillset-blue')
        project = Project.objects.create(title="test project", description="lorem ipsum dolor sit amet.", repo_link="http://google.com", image="someimagehost.com/image.png")
        project.technologies.add(technology)
        response = client.get(reverse('blog:projects'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,technology.name)
        self.assertContains(response,project.title)
        self.assertContains(response,project.description)
        self.assertContains(response,project.repo_link)

    def testMultipleProjects(self):
        client = Client()
        t_python = Technology.objects.create(name='Python', color='.skillset-blue')
        t_java = Technology.objects.create(name='Java', color='.skillset-red')
        t_html = Technology.objects.create(name='HTML', color='.skillset-green')
        project1 = Project.objects.create(title="test project1", description="lorem ipsum dolor sit amet.", repo_link="http://google.com", image="wethsdhg.com/image.png")
        project2 = Project.objects.create(title="test project2", description="loasdrem ipsum dogasdlor sit amet.", repo_link="http://google2.com", image="dfryjdjf.com/image.png")
        project3 = Project.objects.create(title="test3 project3123", description="lorem ipggsum dolor s123git amet.", repo_link="http://google3.com", image="dfg.com/image.png")
        project4 = Project.objects.create(title="test 1312g", description="lorem ipsbum dolor sit amesdt.", repo_link="http://gdfsfg.com", image="ulokgjf.com/image.png")
        project1.technologies.add(t_python,t_java)
        project2.technologies.add(t_python,t_html)
        project3.technologies.add(t_python,t_java)
        project4.technologies.add(t_python,t_java)

        projects = [project1,project2, project3, project4]
        response = client.get(reverse('blog:projects'))

        for project in projects:
            self.assertEqual(response.status_code,200)
            for technology in project.technologies.all():
                self.assertContains(response,technology.name)
            self.assertContains(response,project.title)
            self.assertContains(response,project.description)
            self.assertContains(response,project.repo_link)
