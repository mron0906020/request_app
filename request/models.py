from django.db import models

class Weather(models.Model):

    content = models.CharField(max_length=200)


    def __str__(self):

        return self.content

