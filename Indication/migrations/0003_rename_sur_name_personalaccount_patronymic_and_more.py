# Generated by Django 4.2.4 on 2023-08-22 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Indication', '0002_rename_credentials_personalaccount_first_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personalaccount',
            old_name='sur_name',
            new_name='patronymic',
        ),
        migrations.AlterUniqueTogether(
            name='indication',
            unique_together={('current_value', 'time_of_taking', 'metering_device')},
        ),
        migrations.AlterUniqueTogether(
            name='installedmeteringdevice',
            unique_together={('personal_account', 'metering_device', 'installation_date')},
        ),
        migrations.AlterUniqueTogether(
            name='meteringdevice',
            unique_together={('number', 'model_metering_device', 'date_of_issue')},
        ),
        migrations.AlterUniqueTogether(
            name='metermodel',
            unique_together={('manufacturer', 'model_name')},
        ),
    ]
