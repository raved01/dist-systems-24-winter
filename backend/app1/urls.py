from django.urls import path
from .views import ShoppingItemList, ShoppingItemEdit

urlpatterns = [
    path('', ShoppingItemList.as_view(), name='item-list'),
    path('/<str:name>', ShoppingItemEdit.as_view(), name='item-detail-slash'),

]