from django.core import validators
from django.db import models
from django.core.validators import MinLengthValidator
from django.db.models.base import Model

# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=50)

    def __str__(self):
        return self.caption

class Author(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image_name = models.ImageField(upload_to="posts",null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True ,related_name="posts")
    tags = models.ManyToManyField(Tag)

class registerForVaccine(models.Model):
    name = models.CharField(max_length=255);
    
class Person(models.Model):
    personName = models.CharField(max_length=255)
    age = models.IntegerField(default=0)
    TYPES_OF_VACCINE = (
        ('1', 'فايزر'),
        ('2', 'سبوتنيك'),
        ('3', 'سبوتنيك لايت'),
        ('4', 'موديرنا'),
    )
    typeVaccine = models.CharField(max_length=1, choices=TYPES_OF_VACCINE)
    phone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    TYPES_OF_SICK = (
        ('a', 'نعم'),
        ('b', 'لا'),
    )
    sickBefore = models.CharField(max_length=1, choices=TYPES_OF_SICK)
    notes = models.TextField()

    
# class Admin(models.Model):
#     username = models.CharField(max_length=255)
#     password = models.CharField(max_length=255)