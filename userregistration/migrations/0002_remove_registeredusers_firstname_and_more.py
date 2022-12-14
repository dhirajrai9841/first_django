# Generated by Django 4.0.5 on 2022-07-26 08:52

from django.db import migrations, models
import sqlalchemy.sql.expression


class Migration(migrations.Migration):

    dependencies = [
        ('userregistration', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registeredusers',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='registeredusers',
            name='lastname',
        ),
        migrations.AddField(
            model_name='registeredusers',
            name='Dateofbirth',
            field=models.IntegerField(max_length=10, null=sqlalchemy.sql.expression.true),
            preserve_default=sqlalchemy.sql.expression.true,
        ),
        migrations.AddField(
            model_name='registeredusers',
            name='Reenterpassword',
            field=models.CharField(max_length=225, null=sqlalchemy.sql.expression.true),
            preserve_default=sqlalchemy.sql.expression.true,
        ),
        migrations.AlterField(
            model_name='registeredusers',
            name='email',
            field=models.CharField(max_length=225, null=sqlalchemy.sql.expression.true),
        ),
        migrations.AlterField(
            model_name='registeredusers',
            name='password',
            field=models.CharField(max_length=225, null=sqlalchemy.sql.expression.true),
        ),
        migrations.AlterField(
            model_name='registeredusers',
            name='username',
            field=models.CharField(max_length=225),
        ),
    ]
