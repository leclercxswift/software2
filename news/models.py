from django.db import models

# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=200)
    category_image=models.URLField(max_length = 500,default="https://www.nintenderos.com/wp-content/uploads/2023/02/zelda-tears-loh-e1676061751412.jpg")

    class Meta:
        verbose_name_plural='Categories'

    def __str__(self):
        return self.title

# News Model
class News(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=300)
    image=models.URLField(max_length = 500,default="https://www.nintenderos.com/wp-content/uploads/2023/02/zelda-tears-loh-e1676061751412.jpg")
    detail=models.TextField()
    add_time=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='News'

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    news=models.ForeignKey(News,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    comment=models.TextField()
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.comment
