from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    creator = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_post')
    post_picture = models.ImageField(upload_to='post_pictures',blank=False)
    caption = models.CharField(max_length=100)

    def __str__(self):
        return ("{}".format(self.creator))

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_commenter")
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="post_commented")    
    comment = models.CharField(max_length=200,blank=False)
    
    def __str__(self):
        return ("{} commented on {}".format(self.user,self.post))

class Follow(models.Model):
    follower = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_follower")
    following = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_following")
