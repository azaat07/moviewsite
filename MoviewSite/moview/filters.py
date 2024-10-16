from django_filters.rest_framework import FilterSet
from .models import Movie



class MovieFilter(FilterSet):
    class Meta:
        model = Movie
        fields = {
            'year': ['gt', 'lt'],
            'status_movie': ['exact']
        }