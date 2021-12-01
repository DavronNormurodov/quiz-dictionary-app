# Generated by Django 3.2.9 on 2021-11-30 16:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dictionary', '0003_dictionarymodel_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dictionarymodel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='word_by_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
