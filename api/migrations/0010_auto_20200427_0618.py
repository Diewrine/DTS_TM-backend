# Generated by Django 3.0.5 on 2020-04-27 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_remove_member_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
    ]
