# Generated by Django 3.0.5 on 2020-04-27 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20200427_0618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]