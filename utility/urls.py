from django.urls import path
from utility import views

urlpatterns = [
    path('', views.index, name='index'),   
    path('productform/', views.create_view, name='productform'),
    path('products/', views.products, name='products'),
    path('delete/<id>', views.delete, name='delete'),
    path('update/<id>', views.update_view, name='update'),
    path('update_data', views.updateData, name='updateData')

]