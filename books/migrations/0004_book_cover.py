# Generated by Django 3.1.7 on 2021-03-19 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20210319_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, help_text='Books cover image', upload_to='cover/'),
        ),
    ]