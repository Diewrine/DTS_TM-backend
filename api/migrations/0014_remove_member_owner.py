# Generated by Django 3.0.5 on 2020-05-03 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_member_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='owner',
        ),
    ]
