import django_filters
from django import forms
from django_filters import DateTimeFilter,CharFilter
from django.db import models
from .models import State,City,Country,Account
from blog.models import Post


class PostFilter(django_filters.FilterSet):
    from_date = DateTimeFilter(field_name="created",lookup_expr='gte')
    to_date = DateTimeFilter(field_name='created',lookup_expr='lte')
    Slug = CharFilter(field_name='slug',lookup_expr='icontains')
    class Meta:
        model=Post
        fields = ('status','publish')

class StateFilter(django_filters.FilterSet):
    class Meta:
        model=State
        fields = ['name','country']

class CountryFilter(django_filters.FilterSet):
    class Meta:
        model=Country
        fields='__all__'

class CityFilter(django_filters.FilterSet):
    class Meta:
        model=City
        fields='__all__'

class UserFilter(django_filters.FilterSet):
    username = CharFilter(field_name='username',lookup_expr='icontains')
    class Meta:
        model=Account
        fields=('country','state','city','date_joined')
