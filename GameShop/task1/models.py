from django.db import models

# Create your models here.


class Buyer(models.Model):
    name = models.CharField(max_length=100)  # username аккаунта
    balance = models.DecimalField(max_digits=9, decimal_places=2)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=100)  # Название игры
    cost = models.DecimalField(max_digits=7, decimal_places=2)  # Стоимость
    size = models.DecimalField(max_digits=7, decimal_places=2)  # Размер
    description = models.TextField()  # Описание
    age_limited = models.BooleanField(default=False)  # Возрастное ограничение
    buyer = models.ManyToManyField(Buyer, related_name='game')

    def __str__(self):
        return self.title
