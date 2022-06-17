# Generated by Django 4.0.5 on 2022-06-15 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_contact_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('json_items', models.CharField(default='', max_length=2000)),
                ('name', models.CharField(default='', max_length=100)),
                ('address', models.CharField(default='', max_length=500)),
                ('city', models.CharField(default='', max_length=50)),
                ('state', models.CharField(default='', max_length=50)),
                ('zip', models.CharField(default='', max_length=50)),
            ],
        ),
    ]