from django.urls import path
from .views import ShoppingItemList, ShoppingItemDetail, ShoppingItemCreate, ShoppingItemUpdate, ShoppingItemDelete

urlpatterns = [
    path('items/', ShoppingItemList.as_view(), name='item-list'),
    path('items/<str:name>/', ShoppingItemDetail.as_view(), name='item-detail'),
    path('items/create/', ShoppingItemCreate.as_view(), name='item-create'),
    path('items/update/<str:name>/', ShoppingItemUpdate.as_view(), name='item-update'),
    path('items/delete/<str:name>/', ShoppingItemDelete.as_view(), name='item-delete'),
]