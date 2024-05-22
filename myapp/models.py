from django.db import models

# Create your models here.

class Image(models.Model):
    photo = models.ImageField(upload_to = "myimage")  #it inherits all attributes and methods from fileField but also validates that uploaded object is a valid image
    #  it requires a pillow library. created as varchar in database.
    date = models.DateTimeField(auto_now_add = True)