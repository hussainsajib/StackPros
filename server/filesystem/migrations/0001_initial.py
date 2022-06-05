# Generated by Django 4.0.5 on 2022-06-05 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='FileStructure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('child', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='filesystem.filestructure')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filesystem.filetypes')),
            ],
        ),
    ]