# Generated by Django 4.1.7 on 2023-08-06 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('live_class', '0011_feedback_liveclass'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessonplan',
            name='lesson_data',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
