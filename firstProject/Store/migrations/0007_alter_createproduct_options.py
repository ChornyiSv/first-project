# Generated by Django 4.0 on 2023-12-06 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0006_alter_createproduct_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='createproduct',
            options={'ordering': ('-time_create',)},
        ),
    ]
