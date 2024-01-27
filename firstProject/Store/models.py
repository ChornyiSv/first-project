from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

#функція з вибором категорії під час створення продукту
def topic_fields():
    fields = [
        ('Phones', 'Phones'),
        ('Computers', 'Computers'),
        ('Laptops', 'Laptops'),
        ('Earphones', 'Earphones'),
        ('Furniture', 'Furniture'),
        ('TV', 'TV')
    ]
    return fields

#функція для завантаження файлів
def upload_location(instance, file_name):
    return f'{instance.id}, {file_name}'

#модель створення продуктів
class CreateProduct(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             default=1,
                             on_delete=models.CASCADE
                             )
    topic = models.CharField(max_length=15,
                             choices=topic_fields(),
                             default='')
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to=upload_location,
                              null=True,
                              blank=True,
                              height_field='height_field',
                              width_field='width_field')
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=0)
    time_create = models.DateTimeField(auto_now_add=True)
    site = models.URLField(max_length=100, default='',)

# сортування продуктів за часом створення
    class Meta:
        ordering = ('-time_create',)

# представлення об'єкта в текстовому форматі в даному випадку title
    def __str__(self):
        return self.title

# визначення url адреси об'єкта
    def get_absolute_url(self):
        return f'/store/product_detail/{self.id}'

