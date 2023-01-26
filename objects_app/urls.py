from django.urls import path,include
from .views import item_list


urlpatterns = [
   
    path('item/', item_list),
    
]
