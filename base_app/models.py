from django.db import models
from os import path
from uuid import uuid4


class Home(models.Model):
    title_1 = models.CharField(max_length=40)
    title_2 = models.CharField(max_length=40)
    desc = models.TextField(max_length=200)

    def __str__(self):
        return self.title_1


class Service (models.Model):
    def get_file_name(self, filename):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('images/dishes', filename)
    name = models.CharField(max_length=20, db_index=True)
    icon = models.ImageField(upload_to=get_file_name)
    timer = models.FloatField(default=0.2)
    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.name


class CategoryDish(models.Model):
    name = models.CharField(unique=True, max_length=20, db_index=True)
    position = models.PositiveIntegerField(unique=True)

    class Meta:
        ordering = ('position', )

    def __str__(self):
        return self.name


class About(models.Model):
    desc_1 = models.TextField(max_length=200)
    desc_2 = models.TextField(max_length=200)
    image_1 = models.ImageField()
    image_2 = models.ImageField()
    image_3 = models.ImageField()
    image_4 = models.ImageField()

    def __str__(self):
        return 'About us'


class Dish(models.Model):

    name = models.CharField(max_length=20, db_index=True)
    position = models.PositiveIntegerField()
    is_visible = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    ingredients = models.CharField(max_length=100, blank=True)
    desc = models.CharField(max_length=150, blank=True)
    category = models.ForeignKey(CategoryDish, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}: {self.price}'


class BookTable(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField(max_length=150)
    people = models.PositiveIntegerField()
    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} {self.email}'


class Chef(models.Model):
    photo = models.ImageField(upload_to='images/chef')
    name = models.CharField(max_length=25)
    desc = models.TextField(max_length=60)
    link_facebook = models.CharField(max_length=100, blank=True)
    link_twitter = models.CharField(max_length=100, blank=True)
    link_instagram = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    feedback = models.TextField(max_length=150)
    photo = models.ImageField(upload_to='images/feedback')
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

