from django.db import models

class Maqola(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    content = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
