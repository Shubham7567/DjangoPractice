from django.urls import path
from . import views

app_name='accounts'

urlpatterns=[
    #models
    path('',views.Models,name="models"),
    #country
    path('Country/Add/',views.create_country,name='Add_Country'),
    path('Country/',views.country_list,name='Country_List'),
    path('Country/<int:id>/delete/',views.country_delete,name='contry_delete'),
    path('Country/<int:id>/edit/',views.edit_country,name='country_edit'),
    #state
    path('State/Add/',views.state_create,name='add_state'),
    path('State/',views.state_list,name='state_list'),
    path('State/<int:id>/delete/',views.state_delete,name='delete_state'),
    path('State/<int:id>/edit/',views.edit_state,name='edit_state'),
    #city
    path('City/',views.city_list,name='city_list'),
    path('City/Add/',views.city_add,name='add_city'),
    path('City/<int:id>/edit/',views.city_edit,name='edit_city'),
    path('City/<int:id>/delete/',views.city_delete,name='delete_city'),
    #users
    path('Users/',views.user_list,name='user_list'),
    path('Users/Add/',views.add_user,name='add_user'),
    path('Users/<int:id>/edit/',views.edit_user,name='edit_user'),
    path('Users/<int:id>/delete/',views.delete_user,name='delete_user'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    #posts
    path('posts/',views.post_list,name='post_list'),
    path('posts/add/',views.add_post,name='add_post'),
    path('post/<int:id>/edit',views.edit_post,name='edit_post'),
    path('post/<int:id>/delete/',views.delete_post,name='delete_post'),
]