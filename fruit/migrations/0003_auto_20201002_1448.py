# Generated by Django 3.1.1 on 2020-10-02 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fruit', '0002_auto_20201002_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createqmodel',
            name='start_time',
            field=models.DateTimeField(),
        ),
    ]
