from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views 

urlpatterns = [
    path('',views.index,name='home'),
    path('product_list/',views.list_product,name='list_product'),
    path('product_details/<pk>',views.detail_product,name='detail_product'),
    path('search/', views.search_view, name='product_search'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('terms/',views.terms,name='terms'),
]