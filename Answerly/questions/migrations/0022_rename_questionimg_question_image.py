# Generated by Django 4.2.3 on 2023-10-25 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0021_alter_question_questionimg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='questionimg',
            new_name='image',
        ),
    ]