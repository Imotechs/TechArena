from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from mainapp.models import Software
from PIL import Image
# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    
    student_id = models.CharField(max_length=27,blank=True)
    software = models.ManyToManyField(Software,blank=True)
    image = models.ImageField(default = 'media/default.PNG', upload_to = 'media/profile_pics')    
    def __str__(self):
        return self.student_id

    def get_absolute_url(self):
        return reverse('home')
    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width >300:
            imageparam = (300, 300)
            img.thumbnail(imageparam)
            img.save(self.image.path)


    


