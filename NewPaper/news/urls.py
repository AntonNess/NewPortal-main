from django.urls import path, include
from django.contrib import admin
# Импортируем созданные нами представления
from .views import (PostList, PostSearch, PostDetail, PostCreate, PostUpdate, PostDelete,  UsersUpdate)
urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('', PostList.as_view(), name='post_list'),
   # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
   # int — указывает на то, что принимаются только целочисленные значения
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('search/', PostSearch.as_view(), name='post_search'),
   path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('users/',   UsersUpdate.as_view(), name='users_list'),
  # path('123/', UpdateProfileForm.as_view(), name='users_list'),
#   path('sign/', include('sign.urls')),
 #  path('accounts/', include('allauth.urls')),
]