# Generated by Django 3.1.6 on 2021-02-17 15:33

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('preferences', '0002_auto_20181220_0803'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('preferences_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='preferences.preferences')),
                ('telephone_number', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=100)),
                ('facebook_link', models.CharField(max_length=300)),
                ('instagram_link', models.CharField(max_length=300)),
            ],
            bases=('preferences.preferences',),
            managers=[
                ('singleton', django.db.models.manager.Manager()),
            ],
        ),
    ]