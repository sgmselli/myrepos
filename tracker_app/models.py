from django.db import models

# Create your models here.
class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=30)
    quantity = models.IntegerField()
    price = models.FloatField()

    def get_absolute_url(self):
        return 'list'

    def __str__(self):
        return "INGREDIENT: "+self.ingredient_name+", QUANTITY: "+str(self.quantity)+", PRICE PER UNIT: "+str(self.price)

class MenuItem(models.Model):
    menuitem_name = models.CharField(max_length=100)
    price = models.FloatField()


    def __str__(self):
        return "MENU ITEM: "+self.menuitem_name+",   PRICE PER UNIT: "+str(self.price)
    

class RecipeRequirement(models.Model):
    pass

class Purchase(models.Model):
    pass