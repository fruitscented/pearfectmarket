# Generated by Django 4.1.6 on 2023-11-07 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventblog', '0003_alter_post_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['-name']},
        ),
    ]
