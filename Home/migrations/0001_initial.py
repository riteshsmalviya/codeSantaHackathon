# Generated by Django 4.1.5 on 2023-01-07 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program', models.TextField()),
                ('language', models.CharField(choices=[('c', 'C'), ('c++', 'C++'), ('java', 'Java'), ('python', 'Python'), ('js', 'JavaScript'), ('sql', 'SQL')], default='c', max_length=122)),
                ('code', models.TextField()),
            ],
        ),
    ]
