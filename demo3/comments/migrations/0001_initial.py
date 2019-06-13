# Generated by Django 2.2.2 on 2019-06-13 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pinglun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('pinglun_time', models.DateTimeField(auto_now=True)),
                ('content', models.CharField(max_length=200)),
                ('artical', models.ForeignKey(on_delete=True, to='blog.Artical')),
            ],
        ),
    ]
