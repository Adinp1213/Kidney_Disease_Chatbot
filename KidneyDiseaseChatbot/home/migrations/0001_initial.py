# Generated by Django 4.2.10 on 2024-02-27 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=122)),
                ('password', models.CharField(max_length=122)),
            ],
        ),
        migrations.CreateModel(
            name='FeedBackDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=122)),
                ('feedback', models.CharField(max_length=300)),
                ('response', models.CharField(max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PreviousDetection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=122)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('detection_result', models.CharField(max_length=122)),
                ('input_file', models.FileField(default=None, upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('password', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=13)),
            ],
        ),
    ]
