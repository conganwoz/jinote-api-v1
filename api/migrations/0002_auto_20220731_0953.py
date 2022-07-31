# Generated by Django 3.2.14 on 2022-07-31 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(db_index=True, max_length=500),
        ),
        migrations.AddIndex(
            model_name='note',
            index=models.Index(fields=['alias', 'hashed_unlock_key'], name='api_note_alias_35c769_idx'),
        ),
    ]
