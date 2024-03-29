# Generated by Django 4.1.4 on 2023-01-06 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(default='default.png', upload_to='course_images', verbose_name='Image'),
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(verbose_name='Unique name lesson')),
                ('title', models.CharField(max_length=120, verbose_name='Lesson name')),
                ('desc', models.TextField(verbose_name='About lesson')),
                ('number', models.IntegerField(verbose_name='Number of lesson')),
                ('video', models.CharField(max_length=100, verbose_name='Video URL')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course', verbose_name='Which course?')),
            ],
        ),
    ]
