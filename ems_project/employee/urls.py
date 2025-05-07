from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_employees,name="employee-list"),
    path('create/',views.create_employee,name="employee-create"),
    path('update/<int:pk>/',views.update_employee,name="employee-update"),
    path('delete/<int:pk>/',views.delete_employee,name='employee-delete'),
]