# Generated by Django 4.2.17 on 2025-01-17 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_comment_options_alter_post_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
