from django.urls import path
from .views import index, item, detail_view, create_item, update_item, delete_item


# app_name = 'food'

urlpatterns = [
  #/food
  path('', index, name='index'),
  #/food/1
  path('<int:item_id>/', detail_view, name='detail_view'),
  path('item/', item, name='item'),
  #   add items
  path('add/',create_item, name='create_item'),
  #edit
  path('update/<int:item_id>/', update_item, name='update_item'),
  #delete
  path('delete/<int:item_id>/', delete_item, name='delete_item'),
]