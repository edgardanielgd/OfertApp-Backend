# Generated by Django 3.2.16 on 2023-05-12 19:48

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('publications', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.UUIDField(db_column='repId', default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('type', models.CharField(choices=[('DF', 'Deliveryfraud'), ('SF', 'Suspectfraud'), ('DL', 'Dontlike'), ('MA', 'Misleadingadvertisement'), ('QF', 'Qualityfraud')], db_column='repTitle', max_length=50)),
                ('body', models.TextField(db_column='repBody', max_length=255)),
                ('createdAt', models.DateTimeField(auto_now_add=True, db_column='repCreatedAt')),
                ('open', models.BooleanField(db_column='repOpen', default=True)),
                ('visible', models.BooleanField(db_column='repVisible', default=True)),
                ('publication', models.ForeignKey(db_column='pubId', on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='publications.publication')),
            ],
            options={
                'db_table': 'REPORT',
            },
        ),
        migrations.CreateModel(
            name='ReportSupport',
            fields=[
                ('id', models.UUIDField(db_column='repSopId', default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('body', models.TextField(db_column='repSopBody', max_length=255)),
                ('data', models.FileField(db_column='repSopData', upload_to='reports_support_data')),
                ('createdAt', models.DateTimeField(auto_now_add=True, db_column='repSopCreatedAt')),
                ('visible', models.BooleanField(db_column='repSopVisible', default=True)),
                ('report', models.ForeignKey(db_column='repId', on_delete=django.db.models.deletion.CASCADE, related_name='reports_support', to='reports.report')),
            ],
            options={
                'db_table': 'REPORTSUPPORT',
            },
        ),
    ]
