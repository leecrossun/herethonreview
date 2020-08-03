from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    image = models.ImageField(upload_to='image/')
    pub_date = models.DateTimeField('date published')
    writer = models.CharField(max_length=10, null = True)

    def __str__(self):
        return self.title

    def sum(self):
        return self.body[:100]