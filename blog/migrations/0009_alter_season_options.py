# Generated by Django 4.2.3 on 2023-10-26 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_rename_comment_comment_body_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='season',
            options={'ordering': ['-created_on'], 'verbose_name_plural': 'Season Posts'},
        ),
    ]
