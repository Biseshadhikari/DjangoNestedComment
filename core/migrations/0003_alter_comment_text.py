# Generated by Django 4.1 on 2024-02-10 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_post_comment_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
