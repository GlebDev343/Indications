# Generated by Django 4.2.5 on 2023-09-26 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Indication', '0007_alter_personalaccount_verification_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalaccount',
            name='code_validity',
            field=models.DateTimeField(default='2000-01-01 00:00:00'),
        ),
    ]