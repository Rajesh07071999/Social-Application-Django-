from django.db import models
from django.contrib.auth.models import User




class Comment(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)    
    createtime= models.DateTimeField(auto_now_add=True)
    
   
    
    def __str__(self):
        return self.comment
    
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    images = models.ImageField(upload_to='images')
    createtime= models.DateTimeField(auto_now_add=True)
    uploadtime = models.DateTimeField(auto_now=True)
    Location = models.CharField(max_length=200)
    
   
    
    def __str__(self):
        return self.title
    
    