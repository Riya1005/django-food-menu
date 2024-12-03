from django.urls import path
from . import views

app_name = 'food'
urlpatterns = [
    path('',views.ClassIndexView.as_view(),name='index'),
    path('<int:pk>/',views.ClassDetailView.as_view(),name='detail'),
    path('item/',views.item,name='item'),
    # add item
    path('add',views.CreateItem.as_view(),name='create_item'),
    # update item
    path('update/<int:item_id>/',views.update_item,name='update_item'),
    # delete item
    path('delete/<int:item_id>/',views.delete_item,name='delete_item'),
]

