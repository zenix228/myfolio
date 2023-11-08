from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    author = models.CharField(max_length=250)
    image = models.ImageField(upload_to='posts-images')

    def __str__(self) -> str:
        return self.title
    


