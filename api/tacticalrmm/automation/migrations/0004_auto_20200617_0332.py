# Generated by Django 3.0.7 on 2020-06-17 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automation', '0003_auto_20200609_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policy',
            name='desc',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]