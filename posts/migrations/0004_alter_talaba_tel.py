# Generated by Django 5.1.6 on 2025-03-05 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_talaba_delete_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talaba',
            name='tel',
            field=models.IntegerField(),
        ),
    ]
