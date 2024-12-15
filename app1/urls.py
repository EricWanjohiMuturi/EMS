from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path("", views.employee_list, name="employee_list"),
]