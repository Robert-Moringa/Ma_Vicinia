# Generated by Django 3.2.6 on 2021-09-24 11:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NeighbourHood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default=0)),
                ('county', models.TextField(default=0)),
                ('population', models.IntegerField(default=0)),
                ('description', models.TextField(default=0)),
                ('area_pic_one', models.ImageField(blank=True, default=0, null=True, upload_to='neighbourhood_pics/')),
                ('area_pic_two', models.ImageField(blank=True, default=0, null=True, upload_to='neighbourhood_pics/')),
                ('admin', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'neighbourhood',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, default=0, null=True, upload_to='profile_pics/')),
                ('email', models.TextField(default=0)),
                ('why_here', models.TextField(blank=True, default='What is good abt here?', max_length=200, null=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('nbd', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vicinia.neighbourhood')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'profile',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default=0)),
                ('description', models.TextField(default=0)),
                ('post_pic', models.ImageField(blank=True, default=0, null=True, upload_to='post_pic/')),
                ('contacts', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=254)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('admin', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('nbd', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vicinia.neighbourhood')),
            ],
            options={
                'db_table': 'post',
            },
        ),
        migrations.CreateModel(
            name='Police',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default=0)),
                ('description', models.TextField(default=0)),
                ('pic', models.ImageField(blank=True, default=0, null=True, upload_to='police_pic/')),
                ('contacts', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=254)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('nbd', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vicinia.neighbourhood')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'police',
            },
        ),
        migrations.CreateModel(
            name='Health',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default=0)),
                ('description', models.TextField(default=0)),
                ('pic', models.ImageField(blank=True, default=0, null=True, upload_to='health_pic/')),
                ('contacts', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=254)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('nbd', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vicinia.neighbourhood')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'health',
            },
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default=0)),
                ('description', models.TextField(default=0)),
                ('business_pic_one', models.ImageField(blank=True, default=0, null=True, upload_to='business_pics/')),
                ('business_pic_two', models.ImageField(blank=True, default=0, null=True, upload_to='business_pics/')),
                ('Phone_no', models.IntegerField(default=0)),
                ('email', models.TextField(default=0)),
                ('products', models.TextField(default=0)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('nbd', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vicinia.neighbourhood')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'business',
            },
        ),
    ]