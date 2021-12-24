# Generated by Django 3.2.9 on 2021-12-04 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=150)),
                ('lastName', models.CharField(max_length=250)),
                ('age', models.IntegerField(default=12)),
                ('birthDate', models.DateTimeField()),
            ],
        ),
    ]