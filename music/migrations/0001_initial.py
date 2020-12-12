# Generated by Django 3.1.2 on 2020-12-08 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='unknown', max_length=50)),
                ('country', models.CharField(default='unknown', max_length=50)),
                ('start', models.IntegerField(blank=True, default=1962, null=True, verbose_name='The year the band started playing together')),
                ('end', models.IntegerField(blank=True, default=1962, null=True, verbose_name='The year the band stopped playing together')),
            ],
        ),
    ]
