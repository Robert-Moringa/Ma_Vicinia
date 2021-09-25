# Generated by Django 3.2.6 on 2021-09-25 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vicinia', '0002_auto_20210924_1533'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='admin',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='business',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='business',
            name='name',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='health',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='neighbourhood',
            name='county',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='neighbourhood',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='police',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]