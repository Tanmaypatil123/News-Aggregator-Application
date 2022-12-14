import json
from turtle import heading
from django.utils import timezone
from django.db import models

# Create your models here.

class News_data(models.Model):
    #unique_id = models.CharField(max_length=100, null=True)
    id = models.AutoField(primary_key=True)
    heading = models.CharField(max_length=400,null=True)
    category = models.CharField(max_length=50,null=True)
    img = models.URLField(max_length=300)
    url = models.URLField(max_length=300)
    content = models.CharField(max_length=5000,null=False,default="failed to load data")
    date = models.DateTimeField(timezone.now(),null=True)

    @property
    def to_dict(self):
        data = {
            "data":json.dump({
                "id":self.id,
                "category":self.category,
                "Heading":self.heading,
                "Image_url":self.img ,
                "post_url":self.url,
                "content":self.content
            }),
            "date":self.date
        }
        return data
    def __str__(self):
        return self.heading
      