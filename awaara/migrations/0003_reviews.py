# Generated by Django 3.1.3 on 2020-11-26 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awaara', '0002_destination_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pics')),
                ('review', models.TextField()),
            ],
        ),
    ]
