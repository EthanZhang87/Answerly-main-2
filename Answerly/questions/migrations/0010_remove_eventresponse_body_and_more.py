# Generated by Django 4.2.3 on 2023-10-22 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0009_alter_eventresponse_attending'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventresponse',
            name='body',
        ),
        migrations.RemoveField(
            model_name='eventresponse',
            name='created',
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.TextField(default='America'),
        ),
        migrations.AddField(
            model_name='eventresponse',
            name='notattending',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]