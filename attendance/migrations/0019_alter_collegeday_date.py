# Generated by Django 4.2.4 on 2023-10-06 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0018_attendance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collegeday',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
