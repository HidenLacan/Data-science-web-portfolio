from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name

class Project(models.Model):
    image_url = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    url_project = models.CharField(max_length=300)
    
    