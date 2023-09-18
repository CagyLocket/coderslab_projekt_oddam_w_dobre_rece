from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Institution(models.Model):
    INSTITUTION_TYPES = [
        ('fundacja', 'Fundacja'),
        ('organizacja', 'Organizacja pozarządowa'),
        ('zbiorka', 'Zbiórka lokalna'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=30, choices=INSTITUTION_TYPES, default='fundacja')
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name + ' ---- ' + self.description


class Donation(models.Model):
    quantity = models.PositiveIntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address_street = models.CharField(max_length=255)
    address_number = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField()
    user = models.ForeignKey(User, null=True, default=True,  on_delete=models.SET_NULL)

    def __str__(self):
        return f"Dar nr {self.pk}"


