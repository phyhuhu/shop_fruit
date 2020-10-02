# Generated by Django 3.1.1 on 2020-10-02 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreateQModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=100)),
                ('fruit', models.CharField(choices=[('Apple', 'Apple'), ('Banana', 'Banana'), ('Mango', 'Mango'), ('Grape', 'Grape')], max_length=100)),
                ('quantity', models.IntegerField()),
                ('repeats', models.IntegerField()),
                ('schedule_type', models.CharField(choices=[('Once', 'Once'), ('Minutes', 'Minutes'), ('Hourly', 'Hourly'), ('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly'), ('Quarterly', 'Quarterly'), ('Yearly', 'Yearly'), ('Cron', 'Cron')], max_length=100)),
                ('schedule_quantity', models.IntegerField()),
                ('start_time', models.DateTimeField()),
            ],
        ),
    ]
