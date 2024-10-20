from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    '''
    Creates an instance of the Profile model.

    While no user-specified value for profile_picture, default image by
    Raphael Silva from Pixabay
    https://pixabay.com/vectors/avatar-icon-placeholder-profile-3814049

    '''
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        upload_to='images/',
        default='../default-avatar_nqruck.png'
    )
    made_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-made_at']

    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    '''
    When an instance of User is created, an associated instance of
    Profile is created automatically.
    '''
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
