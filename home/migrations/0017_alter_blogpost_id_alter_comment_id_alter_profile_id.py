# Generated by Django 4.2.3 on 2023-07-28 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_profile_phone_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
