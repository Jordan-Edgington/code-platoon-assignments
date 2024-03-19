from django.db import models

# Create your models here.


class Owner(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField(max_length=2)
    number_of_pets = models.IntegerField(max_length=1)


class Cat(models.Model):
    breed = models.CharField(max_length=25)
    age = models.BigIntegerField(max_length=2)
    vaccinated = models.BooleanField(default=False)
    description = models.TextField(max_length=255)
    name = models.CharField(max_length=25)


class Dog(models.Model):
    breed = models.CharField(max_length=25)
    age = models.BigIntegerField(max_length=2)
    vaccinated = models.BooleanField(default=False)
    description = models.TextField(max_length=255)
    name = models.CharField(max_length=25)


class Bird(models.Model):
    species = models.CharField(max_length=40)
    age = models.BigIntegerField(max_length=2)
    vaccinated = models.BooleanField(default=False)
    description = models.TextField(max_length=255)
    name = models.CharField(max_length=25)


class ExoticAnimal(models.Model):
    region_of_origin = models.CharField(max_length=40)
    age = models.BigIntegerField(max_length=2)
    vaccinated = models.BooleanField(default=False)
    name = models.CharField(max_length=25)
    type_of_animal = models.CharField(max_length=40)
