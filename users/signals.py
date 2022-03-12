from urllib.parse import uses_fragment
from django.db.models.signals import post_save
from .models import User,TpoProfile,CompanyProfile
from django.dispatch import receiver

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        if instance.type=="TPO":
            TpoProfile.objects.create(user=instance)
        elif instance.type=="Company":
            CompanyProfile.objects.create(user=instance)


@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    if instance.type=="TPO":
        instance.tpoprofile.save()
    elif instance.type=="Company":
        instance.companyprofile.save()