# Generated by Django 4.2.4 on 2023-10-02 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0010_remove_enrollment_classinfo_class_enrollments_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='enrollments',
        ),
        migrations.AddField(
            model_name='class',
            name='enrollments',
            field=models.ManyToManyField(blank=True, to='attendance.enrollment'),
        ),
    ]
