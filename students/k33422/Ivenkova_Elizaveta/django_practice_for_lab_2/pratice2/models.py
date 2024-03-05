from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class Owner(AbstractUser):
    birth_date = models.DateField(null=True)
    cars = models.ManyToManyField('Car', through='CarOwnership')
    passport_number = models.CharField(max_length=10,
                                       unique=True,
                                       blank=True,
                                       null=True)
    nationality = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=100, blank=True)

    def get_absolute_url(self):
        return reverse('project_first_app:owner_info', args=[str(self.pk)])

    def __str__(self):
        return f'{self.username}'

class Car(models.Model):
    license_plate = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.license_plate

    def get_absolute_url(self):
        return reverse('pratice2:CarView', kwargs={'pk': self.pk})

# связь между а/м и владельцем = владение
# ассоциативная таблица, связывает 2 исходные.
# тк имеет собственные атрибуты, настраиваем вручную:
class CarOwnership(models.Model):
    # обратная ссылка выглядит как: Owner.ownerships
    # используя .ownerships относительно объекта класса Owner мы получим строку
    # таблицы CarOwnership по данному Owner

    # related name - как это поле будет называться в модели, которую мы указываем как ФК
    # можно жить без этого, но оно полезно
    owner = models.ForeignKey('Owner', on_delete=models.RESTRICT, related_name='ownerships')
    car = models.ForeignKey('Car', on_delete=models.RESTRICT, related_name='ownerships')
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.car} {self.owner}'


class Licence(models.Model):
    number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    data = models.DateField()
    # owner id
    # мб несколько у каждого водителя = many to one
    # FK is always Many-To-One
    owner = models.ForeignKey('Owner', on_delete=models.RESTRICT, related_name='licences')

    def __str__(self):
        return self.number
