# Generated by Django 2.1.5 on 2022-01-07 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='imge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='k_images')),
                ('price', models.PositiveIntegerField()),
                ('des', models.CharField(max_length=200)),
            ],
        ),
    ]
