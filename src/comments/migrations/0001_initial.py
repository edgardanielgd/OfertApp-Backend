# Generated by Django 3.2.16 on 2023-05-12 19:48

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(db_column='comId', default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('text', models.CharField(db_column='comText', max_length=256)),
                ('title', models.CharField(db_column='comTitle', max_length=45, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True, db_column='comCreatedAt')),
            ],
            options={
                'db_table': 'COMMENT',
            },
        ),
        migrations.CreateModel(
            name='Reaction',
            fields=[
                ('id', models.UUIDField(db_column='reacId', default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('type', models.CharField(choices=[('LIKE', 'Like'), ('DISLIKE', 'Dislike'), ('WARNING', 'Warning')], db_column='reacType', max_length=45)),
                ('createdAt', models.DateTimeField(auto_now_add=True, db_column='reacCreatedAt')),
                ('comment', models.ForeignKey(db_column='comId', on_delete=django.db.models.deletion.CASCADE, related_name='reactions', to='comments.comment')),
            ],
            options={
                'db_table': 'REACTION',
            },
        ),
    ]
