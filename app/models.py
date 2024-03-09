from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Recipe(models.Model):

    title = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    meal_type = models.CharField(max_length=50)
    ingredients = models.TextField()

    def __str__(self):
        return self.title


class Review(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    reviews=models.TextField()
    rating=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.recipe.title