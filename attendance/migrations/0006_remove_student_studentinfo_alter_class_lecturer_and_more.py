# Generated by Django 4.2.4 on 2023-09-25 21:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('attendance', '0005_student_lecturer_alter_class_lecturer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='studentInfo',
        ),
        migrations.AlterField(
            model_name='class',
            name='lecturer',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='collegeday',
            name='students',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='student',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Lecturer',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
