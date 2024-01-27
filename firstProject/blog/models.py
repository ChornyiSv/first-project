from django.conf import settings
from django.db import models

def topic_fields():
    fields = [
        ('життя', 'життя'),
        ('nature', 'nature'),
        ('animals', 'тварини'),
        ('жарти', 'joke')

    ]
    return fields

def upload_location(instance, file_name):
    return f'{instance.id}, {file_name}'

class Post(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             default=1,
                             on_delete=models.CASCADE
                             )
    topic = models.CharField(max_length=15,
                             choices= topic_fields(),
                             default='')
    title = models.CharField(max_length=40)
    content = models.TextField()
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    # Integer field, поле типу integer, використаємо його для опису ціна за ноутбук, по дефолту значення 0
    # при створенні поста можна  його змінити, відображається на головній сторінці аплікації
    price = models.IntegerField(default=0)
    # URLField поле типу str, в даному випадку з обмеженою кількістю символів до 100
    # URL адреса корисне полe при потребі додати посилання на сайт чи річ яку можна придбати
    site = models.URLField(max_length=100, default='Write url - address of site where u can buy the product!')
    image = models.ImageField(upload_to=upload_location,
                              null=True,
                              blank=True,
                              height_field='height_field',
                              width_field='width_field')
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    class Meta:
        ordering =('-timestamp',)

    def get_absolute_url(self):
        return f'/blog/detail/{self.id}'

    def __str__(self): # повертаємо тайтл в форматі стрічки
        return self.title

#Post.objects.all()