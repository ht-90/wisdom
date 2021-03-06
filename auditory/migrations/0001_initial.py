# Generated by Django 3.1.7 on 2021-03-14 05:36

import auditory.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('audiofile', models.FileField(upload_to='', validators=[auditory.validators.validate_file_extension, auditory.validators.validate_file_size])),
            ],
        ),
    ]
