# Generated by Django 4.0.5 on 2022-08-15 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_checklist_notes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checklist',
            old_name='start_date',
            new_name='date',
        ),
    ]
