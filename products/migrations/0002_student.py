# Generated by Django 2.0.2 on 2019-01-15 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email_id', models.EmailField(max_length=50)),
                ('contact_no', models.CharField(max_length=11)),
                ('dat', models.DateTimeField()),
            ],
        ),
    ]
