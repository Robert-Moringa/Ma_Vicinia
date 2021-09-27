from django.db import models
from django.contrib.auth.models import User
from registration.signals import user_registered
from django.dispatch import receiver
from .email import send_welcome_email
from django.http  import HttpResponse, JsonResponse
from registration.signals import user_activated
from django.dispatch import receiver
from django.core.mail import send_mail



@receiver(user_registered)
def user_signed_up_( user, **kwargs):
    name = user.username
    email = user.email
    
    send_welcome_email(name, email)
    data = {'success': 'Welcome to the Ma_Vicinia application.'}
    return JsonResponse(data)
    

# Create your models here.
class NeighbourHood(models.Model):
    class Meta:
        db_table = 'neighbourhood'
    name= models.CharField(max_length=40)
    county=models.CharField(max_length=40)
    population=models.IntegerField()
    description= models.TextField()
    area_pic_one = models.ImageField(upload_to='neighbourhood_pics/', null=True, blank=True)
    area_pic_two = models.ImageField(upload_to='neighbourhood_pics/', null=True, blank=True)
    admin=models.ForeignKey(User, on_delete=models.CASCADE, null=True)


    def create_neigborhood(sender, instance, created, **kwargs):
        if created:
            NeighbourHood.objects.create(user=instance)


    def save_neigborhood(self):
        self.save()

    def delete_neigborhood(self):
        self.delete()

    def find_neigborhood(cls,nbd_id):
        nbd= cls.objects.filter(id=nbd_id)
        return nbd

    def find_neigborhd(cls,nbd_id):
        nbd= cls.objects.filter(id=nbd_id)
        return nbd.name

    @classmethod
    def update_occupants(self, update):
        self.population=update
        self.save()

    @property
    def image_url(self):
        if self.area_pic_one and hasattr(self.area_pic_one, 'url'):
            return self.area_pic_one.url

    def __str__(self):
        return self.name

class Profile(models.Model):
    class Meta:
        db_table = 'profile'

    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    email= models.EmailField()
    pub_date = models.DateTimeField(auto_now_add=True)
    nbd= models.ForeignKey(NeighbourHood, null=True, blank=True, on_delete=models.CASCADE)
    why_here= models.TextField(max_length=200, null=True, blank=True, verbose_name='What do you like about the above neighbourhood?')
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)


    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def get_profile(cls, user):
        profile = cls.objects.filter(user=user)
        return profile

    @classmethod
    def search_users(cls, search_term):
        profiles = cls.objects.filter(user__username__icontains=search_term)
        return profiles

    @property
    def image_url(self):
        if self.profile_pic and hasattr(self.profile_pic, 'url'):
            return self.profile_pic.url

    def __str__(self):
        return self.user.username

class Business(models.Model):
    class Meta:
        db_table = 'business'
    name= models.CharField(max_length=70)
    description= models.TextField()
    business_pic_one = models.ImageField(upload_to='business_pics/', null=True, blank=True)
    business_pic_two = models.ImageField(upload_to='business_pics/', null=True, blank=True)
    Phone_no= models.IntegerField(default=0)
    email= models.EmailField()
    products= models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    nbd=models.ForeignKey(NeighbourHood, null=True, blank=True, on_delete=models.CASCADE)

    def create_business(sender, instance, created, **kwargs):
        if created:
            Business.objects.create(user=instance)


    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    def find_business(cls,business_id):
        business= cls.objects.filter(user=business_id)
        return business

    @classmethod
    def update_business(self, update):
        self.name=update
        self.save()

    @property
    def image_url(self):
        if self.business_pic_one and hasattr(self.business_pic_one, 'url'):
            return self.business_pic_one.url

    def __str__(self):
        return self.name


class Post(models.Model):
    class Meta:
        db_table = 'post'
    title= models.CharField(max_length=40)
    description=models.TextField()
    post_pic= models.ImageField(upload_to='post_pic/', null=True, blank=True)
    contacts=models.IntegerField(default=0)
    email=models.EmailField()
    nbd=models.ForeignKey(NeighbourHood, null=True, blank=True, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    @classmethod
    def save_post(self):
        self.save()

    @classmethod
    def delete_post(self):
        self.delete()

    @classmethod
    def find_post(cls,nbd_id):
        post= cls.objects.filter(user=nbd_id)
        return post

    @classmethod
    def find_post(cls,user):
        post= cls.objects.filter(user=user)
        return post

    def __str__(self):
        return self.title


class Health(models.Model):
    class Meta:
        db_table = 'health'
    name= models.CharField(max_length=40)
    description=models.TextField()
    pic= models.ImageField(upload_to='health_pic/', null=True, blank=True)
    contacts=models.IntegerField(default=0)
    email=models.EmailField()
    nbd=models.ForeignKey(NeighbourHood, null=True, blank=True, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    @classmethod
    def save_health(self):
        self.save()

    @classmethod
    def delete_health(self):
        self.delete()

    @classmethod
    def find_health(cls,nbd_id):
        post= cls.objects.filter(user=nbd_id)
        return post


    def __str__(self):
        return self.name

class Police(models.Model):
    class Meta:
        db_table = 'police'
    name= models.CharField(max_length=40)
    description=models.TextField()
    pic= models.ImageField(upload_to='police_pic/', null=True, blank=True)
    contacts=models.IntegerField(default=0)
    email=models.EmailField()
    nbd=models.ForeignKey(NeighbourHood, null=True, blank=True, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    @classmethod
    def save_police(self):
        self.save()

    @classmethod
    def delete_police(self):
        self.delete()

    @classmethod
    def find_police(cls,nbd_id):
        post= cls.objects.filter(user=nbd_id)
        return post


    def __str__(self):
        return self.name