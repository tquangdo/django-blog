# Generated by Django 3.1.1 on 2020-10-02 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_dotq', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
