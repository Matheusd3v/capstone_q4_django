# Generated by Django 4.0.4 on 2022-05-30 18:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('brand_uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('site', models.CharField(max_length=255, null=True)),
            ],
            options={
                'verbose_name_plural': 'brands',
            },
        ),
    ]
