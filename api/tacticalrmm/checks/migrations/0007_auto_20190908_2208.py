# Generated by Django 2.2.4 on 2019-09-08 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checks', '0006_auto_20190908_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='standardcheck',
            name='status',
            field=models.CharField(choices=[('passing', 'Passing'), ('failing', 'Failing'), ('pending', 'Pending')], default='pending', max_length=30),
        ),
    ]