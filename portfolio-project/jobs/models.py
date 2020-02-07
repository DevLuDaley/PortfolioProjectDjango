from django.db import models


class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
   # url = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.summary
