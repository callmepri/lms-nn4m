# Generated by Django 4.1.7 on 2023-03-21 02:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0014_remove_ucatvideo_thumbnail'),
        ('Forum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='forum',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='general.ucatvideo'),
        ),
    ]
