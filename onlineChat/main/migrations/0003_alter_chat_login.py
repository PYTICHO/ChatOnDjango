# Generated by Django 4.1.3 on 2023-01-28 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_chat_options_alter_message_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='login',
            field=models.CharField(max_length=300, unique=True, verbose_name='Логин'),
        ),
    ]
