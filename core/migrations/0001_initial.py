# Generated by Django 2.1.2 on 2018-10-21 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cidade',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('data_insercao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]