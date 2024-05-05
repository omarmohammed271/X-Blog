import uuid
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

def image_upload(instance,filename:str):
    extension = filename.split('.')[1]
    return f'profiles/{instance.user}.{extension}'
class Profile(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload, blank=True,null=True)
    phone = models.CharField(max_length=15)

    def __str__(self) -> str:
        return str(self.user)


@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)