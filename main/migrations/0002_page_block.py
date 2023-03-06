# Generated by Django 4.1.4 on 2023-03-06 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('header', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Текст', 'Text'), ('Изображение', 'Image')], default='Текст', max_length=255)),
                ('text', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='pages')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.page')),
            ],
        ),
    ]