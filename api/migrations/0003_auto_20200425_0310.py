# Generated by Django 3.0.5 on 2020-04-25 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='created_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='member',
            name='updated_at',
            field=models.DateTimeField(),
        ),
    ]