# Generated by Django 3.2.6 on 2021-09-24 15:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vicinia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='business_pic_one',
            field=models.ImageField(blank=True, null=True, upload_to='business_pics/'),
        ),
        migrations.AlterField(
            model_name='business',
            name='business_pic_two',
            field=models.ImageField(blank=True, null=True, upload_to='business_pics/'),
        ),
        migrations.AlterField(
            model_name='business',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='business',
            name='email',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='business',
            name='name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='business',
            name='products',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='business',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='health',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='health',
            name='name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='health',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='health_pic/'),
        ),
        migrations.AlterField(
            model_name='health',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='neighbourhood',
            name='admin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='neighbourhood',
            name='area_pic_one',
            field=models.ImageField(blank=True, null=True, upload_to='neighbourhood_pics/'),
        ),
        migrations.AlterField(
            model_name='neighbourhood',
            name='area_pic_two',
            field=models.ImageField(blank=True, null=True, upload_to='neighbourhood_pics/'),
        ),
        migrations.AlterField(
            model_name='neighbourhood',
            name='county',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='neighbourhood',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='neighbourhood',
            name='name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='neighbourhood',
            name='population',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='police',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='police',
            name='name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='police',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='police_pic/'),
        ),
        migrations.AlterField(
            model_name='police',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='admin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_pic',
            field=models.ImageField(blank=True, null=True, upload_to='post_pic/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='why_here',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]