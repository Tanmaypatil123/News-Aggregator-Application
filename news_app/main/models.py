import json
from turtle import heading
from django.utils import timezone
from django.db import models

# Create your models here.

class News_data(models.Model):
    #unique_id = models.CharField(max_length=100, null=True)
    heading = models.CharField(max_length=400,null=True)
    img = models.URLField(max_length=300)
    url = models.URLField(max_length=300)
    date = models.DateTimeField(timezone.now(),null=True)

    @property
    def to_dict(self):
        data = {
            "data":json.dump({
                "Heading":self.heading,
                "Image_url":self.img ,
                "post_url":self.url
            }),
        }
        return data
    def __str__(self):
        return self.heading