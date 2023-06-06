from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save

# Create your models here.
class Perfil(models.Model):
    
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    image= models.URLField(max_length = 500,default="https://cdn2.excelsior.com.mx/media/styles/grande/public/pictures/2023/02/03/2898189.jpg")
    def __str__(self) -> str:
        return f' Usuario de {self.user.username}'
    def following(self):
        user_ids = Relationship.objects.filter(from_user=self.user).values_list('to_user_id', flat=True)
        following_users = User.objects.filter(id__in=user_ids)
        following_usernames = [user.username for user in following_users]
        return following_usernames
    def followers(self):
        user_ids= Relationship.objects.filter(to_user=self.user)\
                                            .values_list('from_user_id',flat= True)
        return User.objects.filter(id__in=user_ids)
        
class Publicaciones(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="publicaciones")
    timestamp= models.DateTimeField(default=timezone.now)
    content= models.TextField()
    class Meta:
        ordering=['-timestamp']
        def __str__(self):
            return f'{self.user.username}:{self.content}'
def create_profile(sender,instance,created,**kwargs):
    if created:
        Perfil.objects.create(user=instance)
post_save.connect(create_profile, sender=User)





class Relationship(models.Model):
    from_user = models.ForeignKey(User, related_name='relationships', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='related_to', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.from_user} to {self.to_user}'

    class Meta:
        indexes = [
            models.Index(fields=['from_user', 'to_user']),
        ]

 
