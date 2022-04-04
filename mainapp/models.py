from django.db import models
from PIL import Image
# Create your models here.
class Software(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now=True)
    image = models.ImageField(default = 'media/soft.PNG', upload_to = 'media/software_profile')    

    def __str__(self):
        return self.name
    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width >300:
            imageparam = (300, 300)
            img.thumbnail(imageparam)
            img.save(self.image.path)