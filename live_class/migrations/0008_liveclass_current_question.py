# Generated by Django 4.1.7 on 2023-08-01 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('live_class', '0007_liveclass_lesson_data_liveclass_lesson_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='liveclass',
            name='current_question',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
