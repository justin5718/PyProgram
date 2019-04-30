# Generated by Django 2.2 on 2019-04-25 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=200)),
                ('pub_time', models.DateTimeField(verbose_name='date up')),
            ],
        ),
        migrations.CreateModel(
            name='text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_raw', models.CharField(max_length=200)),
                ('text_processed', models.CharField(max_length=200)),
                ('language', models.CharField(max_length=20)),
                ('wav', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recorder.Wav')),
            ],
        ),
    ]