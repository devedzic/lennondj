# Generated by Django 3.1.2 on 2020-12-08 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='end',
            field=models.IntegerField(blank=True, default=1970, null=True, verbose_name='The year the band stopped playing together'),
        ),
    ]
