from django.db import models

class Product(models.Model):
    name = models.CharField(max_length = 50)
    model = models.CharField(max_length = 30)
    price = models.PositiveIntegerField()


    MOBILE = 1
    LAPTOP = 2

    category_choice = (
        (MOBILE, 'Mobile'),
        (LAPTOP, 'Laptop'),
    )

    category = models.IntegerField(choices = category_choice)

    def __str__(self):
        return self.name
