# Generated by Django 4.0.4 on 2022-06-22 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0006_alter_worker_manager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='manager',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='workers.worker'),
        ),
    ]
