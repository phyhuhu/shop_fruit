# Generated by Django 3.1.1 on 2020-10-02 15:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fruit', '0003_auto_20201002_1448'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreateTaskModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=100)),
                ('fruit', models.CharField(choices=[('Apple', 'Apple'), ('Banana', 'Banana'), ('Mango', 'Mango'), ('Grape', 'Grape')], max_length=100)),
                ('quantity', models.IntegerField()),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
