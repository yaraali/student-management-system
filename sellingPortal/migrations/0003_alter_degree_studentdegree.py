# Generated by Django 3.2.9 on 2021-12-04 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellingPortal', '0002_degree'),
    ]

    operations = [
        migrations.AlterField(
            model_name='degree',
            name='studentDegree',
            field=models.FloatField(null=True),
        ),
    ]
