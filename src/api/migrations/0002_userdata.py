# Generated by Django 3.0.4 on 2020-03-20 10:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='userData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('transactionHash', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('userId', models.IntegerField(unique=True)),
                ('first_name', models.CharField(max_length=255)),
                ('middle_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('phoneNumber', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]