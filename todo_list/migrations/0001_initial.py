# Generated by Django 4.1.7 on 2023-04-03 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('creation_time', models.DateTimeField()),
                ('deadline', models.DateTimeField(null=True)),
                ('complete', models.BooleanField(default=False)),
                ('tags', models.ManyToManyField(related_name='tasks', to='todo_list.tag')),
            ],
        ),
    ]
