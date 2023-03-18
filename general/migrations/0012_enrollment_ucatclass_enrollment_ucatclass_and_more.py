# Generated by Django 4.1.7 on 2023-03-14 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0011_alter_ucatstudent_tasks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrollment_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UcatClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('students', models.ManyToManyField(through='general.Enrollment', to='general.ucatstudent')),
            ],
        ),
        migrations.AddField(
            model_name='enrollment',
            name='UcatClass',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.ucatclass'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.ucatstudent'),
        ),
        migrations.AddField(
            model_name='ucatstudent',
            name='ucatClass',
            field=models.ManyToManyField(through='general.Enrollment', to='general.ucatclass'),
        ),
    ]
