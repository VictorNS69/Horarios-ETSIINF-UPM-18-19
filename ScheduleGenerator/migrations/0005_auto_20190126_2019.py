# Generated by Django 2.1.5 on 2019-01-26 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ScheduleGenerator', '0004_auto_20190124_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='type',
            field=models.CharField(choices=[('Básica', 'Básica'), ('Obligatoria', 'Obligatoria'), ('Opcional', 'Opcional')], max_length=10),
        ),
    ]
