# Generated by Django 3.0.4 on 2020-03-29 01:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('bio', models.CharField(blank=True, max_length=250)),
                ('email_address', models.CharField(blank=True, max_length=50)),
                ('email_verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('name', models.CharField(max_length=50)),
                ('event_link', models.CharField(max_length=250)),
                ('contribution_link', models.CharField(blank=True, max_length=250)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sfys_app.Artist')),
                ('genre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sfys_app.Genre')),
            ],
        ),
    ]
