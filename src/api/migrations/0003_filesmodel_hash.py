# Generated by Django 3.0.4 on 2020-03-20 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_userdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='filesmodel',
            name='hash',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
