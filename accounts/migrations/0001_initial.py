# Generated by Django 3.1.2 on 2020-11-09 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.TextField(max_length=100)),
                ('title', models.TextField(max_length=100)),
                ('content', models.TextField(max_length=10000)),
            ],
        ),
    ]