# Generated by Django 5.2.4 on 2025-07-25 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_post_title_post_theme_alter_post_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='theme',
        ),
    ]
