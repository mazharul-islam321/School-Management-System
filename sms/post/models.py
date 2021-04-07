from django.db import models
from django.urls import reverse



class Post(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField()
  image = models.ImageField()

  def __str__(self):
        return self.title
 
  def get_absolute_url(self):
        return reverse('post-detail', kwargs={
            'id': self.id
        })