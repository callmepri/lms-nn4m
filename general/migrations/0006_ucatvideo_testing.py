# Generated by Django 4.1.7 on 2023-02-17 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0005_ucatvideo_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='ucatvideo',
            name='testing',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
