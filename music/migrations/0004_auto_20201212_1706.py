# Generated by Django 3.1.2 on 2020-12-12 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_musician'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musician',
            name='alive',
            field=models.BooleanField(choices=[('ALIVE', 'alive'), ('DECEASED', 'deceased')], default='alive', verbose_name='Alive/Deceased'),
        ),
    ]