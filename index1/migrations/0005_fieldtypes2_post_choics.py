# Generated by Django 4.0.5 on 2022-07-06 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index1', '0004_fieldtypes2'),
    ]

    operations = [
        migrations.AddField(
            model_name='fieldtypes2',
            name='post_choics',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
