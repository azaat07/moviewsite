# Generated by Django 5.1.1 on 2024-10-12 20:04

import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor_name', models.CharField(max_length=32)),
                ('bio', models.TextField(blank=True, null=True)),
                ('age', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('actor_image', models.ImageField(blank=True, null=True, upload_to='actor_image/')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=16, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('director_name', models.CharField(max_length=255)),
                ('bio', models.TextField(blank=True, null=True)),
                ('age', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('director_image', models.ImageField(blank=True, null=True, upload_to='directors/')),
            ],
        ),
        migrations.CreateModel(
            name='Janre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('janre_name', models.CharField(blank=True, max_length=32, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=255)),
                ('movie_name_en', models.CharField(max_length=255, null=True)),
                ('movie_name_ru', models.CharField(max_length=255, null=True)),
                ('movie_name_ky', models.CharField(max_length=255, null=True)),
                ('year', models.PositiveIntegerField()),
                ('movie_time', models.DurationField()),
                ('description', models.TextField(max_length=100)),
                ('description_en', models.TextField(max_length=100, null=True)),
                ('description_ru', models.TextField(max_length=100, null=True)),
                ('description_ky', models.TextField(max_length=100, null=True)),
                ('movie_trailer', models.URLField()),
                ('movie_image', models.ImageField(blank=True, null=True, upload_to='movies/')),
                ('status_movie', models.CharField(choices=[('pro', 'Pro'), ('simple', 'Simple')], max_length=10)),
                ('type', models.IntegerField(choices=[(144, '144p'), (360, '360p'), (480, '480p'), (720, '720p'), (1080, '1080p')])),
                ('actor', models.ManyToManyField(related_name='actors', to='moview.actor')),
                ('country', models.ManyToManyField(related_name='countrys', to='moview.country')),
                ('director', models.ManyToManyField(related_name='directors', to='moview.director')),
                ('janre', models.ManyToManyField(related_name='Janre', to='moview.janre')),
            ],
        ),
        migrations.CreateModel(
            name='Moments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_moment', models.FileField(upload_to='movie_moments/')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='moments', to='moview.movie')),
            ],
        ),
        migrations.CreateModel(
            name='MovieLanguages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=50)),
                ('video', models.FileField(upload_to='movie_videos/')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_languages', to='moview.movie')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('age', models.PositiveSmallIntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(18), django.core.validators.MaxValueValidator(90)])),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region='KG')),
                ('status', models.CharField(choices=[('pro', 'Pro'), ('simple', 'Simple')], max_length=10)),
                ('groups', models.ManyToManyField(blank=True, related_name='userprofile_groups', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='userprofile_permissions', to='auth.permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], verbose_name='ratings')),
                ('text', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='moview.movie')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='replies', to='moview.rating')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='moview.userprofile')),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='moview.userprofile'),
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('viewed_at', models.DateTimeField(auto_now_add=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history', to='moview.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moview.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteMovie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='in_favorites', to='moview.movie')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_movies', to='moview.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='moview.userprofile')),
            ],
        ),
    ]
