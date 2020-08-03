from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Blog(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    image = models.ImageField(upload_to='image/')
    pub_date = models.DateTimeField('date published')
    writer = models.CharField(max_length=10, null = True)
    thumnail = ImageSpecField(source='image', processors=[ResizeToFill(200, 150)])

    def __str__(self):
        return self.title

    def sum(self):
        return self.body[:50]