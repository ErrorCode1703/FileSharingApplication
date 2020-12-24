# Generated by Django 3.1.1 on 2020-10-22 18:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multi_email_field.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('fileID', models.TextField(primary_key=True, serialize=False)),
                ('fileName', models.TextField(max_length=150)),
                ('secretKey', models.TextField(default='')),
                ('driveID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.drive')),
            ],
        ),
        migrations.CreateModel(
            name='ShareFile',
            fields=[
                ('shareFileID', models.TextField(primary_key=True, serialize=False)),
                ('editable', models.IntegerField(choices=[(0, 'Deny'), (1, 'Accept')], default=0)),
                ('printable', models.IntegerField(choices=[(0, 'Deny'), (1, 'Accept')], default=0)),
                ('secretKey', models.TextField()),
                ('passLink', models.TextField()),
                ('shareEmails', multi_email_field.fields.MultiEmailField(default=[])),
                ('share_file_name', models.TextField()),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('file_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.file')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
