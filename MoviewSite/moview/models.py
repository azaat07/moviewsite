from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField

from django.contrib.auth.models import AbstractUser, User


class UserProfile(AbstractUser):

    age = models.PositiveSmallIntegerField(default=0, null=True, blank=True,
                                           validators=[MinValueValidator(18), MaxValueValidator(90)])
    phone_number = PhoneNumberField(null=True, blank=True, region='KG')
    STATUS_CHOICES = (
        ('pro', 'Pro'),
        ('simple', 'Simple'),
    )

    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='userprofile_groups',  # Уникальное имя для обратной ссылки
        blank=True
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='userprofile_permissions',  # Уникальное имя для обратной ссылки
        blank=True
    )

    def __str__(self):
        return f' {self.first_name} - {self.last_name}'


class Country(models.Model):
    country_name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.country_name


class Director(models.Model):
    director_name = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    director_image = models.ImageField(upload_to='directors/', blank=True, null=True)

    def __str__(self):
        return self.director_name


class Actor(models.Model):
    actor_name = models.CharField(max_length=32)
    bio = models.TextField(blank=True, null=True)
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    actor_image = models.ImageField(upload_to='actor_image/', blank=True, null=True)

    def __str__(self):
        return self.actor_name


class Janre(models.Model):
    janre_name = models.CharField(max_length=32, null=True, blank=True)


    def __str__(self):
        return self.janre_name


class Movie(models.Model):
    movie_name = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    country = models.ManyToManyField(Country, related_name='countrys')
    director = models.ManyToManyField(Director,  related_name='directors')
    actor = models.ManyToManyField(Actor, related_name='actors')
    #actor = models.ForeignKey('Actor', on_delete=models.CASCADE, default=1)
    janre = models.ManyToManyField(Janre, related_name='Janre')
    movie_time = models.DurationField()
    description = models.TextField(max_length=100)
    movie_trailer = models.URLField()
    movie_image = models.ImageField(upload_to='movies/', blank=True, null=True)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True)


    MOVIE_TYPES = [
        (144, '144p'),
        (360, '360p'),
        (480, '480p'),
        (720, '720p'),
        (1080, '1080p'),
    ]
    STATUS_CHOICES = [
        ('pro', 'Pro'),
        ('simple', 'Simple'),
    ]
    status_movie = models.CharField(max_length=10, choices=STATUS_CHOICES)
    type = models.IntegerField(choices=MOVIE_TYPES)

    def __str__(self):
        return self.movie_name


class MovieLanguages(models.Model):
    language = models.CharField(max_length=50)
    video = models.FileField(upload_to='movie_videos/')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_languages')

    def __str__(self):
        return self.language


class Moments(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='moments')
    movie_moment = models.FileField(upload_to='movie_moments/')


class Rating(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='ratings')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], verbose_name="ratings")
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='replies')
    text = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)


class Favorite(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='favorites')
    created_date = models.DateTimeField(auto_now_add=True)


class FavoriteMovie(models.Model):
    cart = models.ForeignKey(UserProfile, related_name='favorite_movies', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='in_favorites', on_delete=models.CASCADE)


class History(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='history', on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(auto_now_add=True)



