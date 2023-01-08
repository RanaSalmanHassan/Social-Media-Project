from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='user_profile')
    # sno = models.IntegerField(primary_key=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True,null=True)
    webiste = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    location = models.TextField(blank=True, null=True)

    def __str__(self):
        return ('{}'.format(self.user))

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.user_profile.save()
