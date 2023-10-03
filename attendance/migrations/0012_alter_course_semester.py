# Generated by Django 4.2.4 on 2023-10-03 01:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0011_remove_class_enrollments_class_enrollments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='attendance.semester'),
        ),
    ]
