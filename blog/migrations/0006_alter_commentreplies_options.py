# Generated by Django 4.2.3 on 2023-10-25 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_commentreplies'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commentreplies',
            options={'ordering': ['created_on'], 'verbose_name_plural': 'Replies'},
        ),
    ]