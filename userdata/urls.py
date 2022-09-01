from django.urls import path
from userdata import views

urlpatterns = [
    path("",views.ListTodoAPIView.as_view(),name="userdata_list"),
    path("create/", views.CreateTodoAPIView.as_view(),name="userdata_create"),
    path("update/<int:pk>/",views.UpdateTodoAPIView.as_view(),name="update_userdata"),
    path("delete/<int:pk>/",views.DeleteTodoAPIView.as_view(),name="delete_userdata")
]