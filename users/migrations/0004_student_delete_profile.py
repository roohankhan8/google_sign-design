# Generated by Django 4.2.2 on 2023-06-29 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_delete_writer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=100)),
                ('l_name', models.CharField(max_length=100)),
                ('excited', models.CharField(max_length=255)),
                ('time', models.CharField(max_length=255)),
                ('book', models.CharField(max_length=100)),
                ('food', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
