# Generated by Django 3.0.5 on 2020-04-29 01:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0012_auto_20200427_0622'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='member', to=settings.AUTH_USER_MODEL),
        ),
    ]
