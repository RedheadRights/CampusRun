# Generated by Django 4.0.2 on 2022-03-19 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapIntegration', '0006_alter_route_addr1_alter_route_addr2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='route',
            name='addr1',
        ),
        migrations.RemoveField(
            model_name='route',
            name='addr2',
        ),
    ]
